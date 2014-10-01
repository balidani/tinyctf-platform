#!/usr/bin/env python

"""task_import.py -- imports tasks from 'tasks.json' into the database"""

import dataset
import json
import sys

if __name__ == '__main__':

    purge = False

    # Handle the optional purge argument
    if len(sys.argv) > 1:
        if sys.argv[1] == 'purge':

            purge = True
            print "[*] Purge mode is on, old tasks deleted"

    # Load the json structure
    tasks_str = open('tasks.json', 'rb').read()
    tasks_json = json.loads(tasks_str)

    # Connect to database
    db = dataset.connect('sqlite:///ctf.db')
    cat_table = db['categories']
    tasks_table = db['tasks']
    cat_task_table = db['cat_task']

    if purge:
        cat_table.delete()
        tasks_table.delete()
        cat_task_table.delete()

    # Parse the json file and add rows to the table
    old_cat_count = len(list(cat_table))
    old_task_count = len(list(tasks_table))

    # First, create categories
    for category in tasks_json['categories']:

        cat = category.copy()
        del cat['tasks']
        
        if cat_table.find_one(id=cat['id']):

            # Update existing category
            cat_table.update(cat, ['id'])

        else:
            cat_table.insert(cat)

    new_cat_count = len(list(cat_table))
    print "[*] Imported %d new categories" % (new_cat_count - old_cat_count)

    # Then create tasks
    for category in tasks_json['categories']:
        for task in category['tasks']:
            
            if tasks_table.find_one(id=task['id']):

                # Update existing table
                tasks_table.update(task, ['id'])
            else:
                tasks_table.insert(task)

                # In this case, we should add an entry to the category_task table as well
                row = dict(cat_id=category['id'], task_id=task['id'])
                cat_task_table.insert(row)

    new_task_count = len(list(tasks_table))
    print "[*] Imported %d new tasks" % (new_task_count - old_task_count)