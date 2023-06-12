from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

def load_data(): # open the csv file in read mode
    data = []
    with open('example_batch_records.csv', 'r', encoding="utf-8-sig") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

@app.route('/batch_jobs', methods=['GET']) # decorater for the URL route
def get_batch_jobs():
    data = load_data()

    filter_params = request.args.to_dict() # convert data to dictionary of series. assuming that the
                                           # format of filter isn't comma separated values then necessary changes
                                           # need to be done to how filter is working
    filtered_data = data.copy()
    # the key-value pairs are in the "filters" dictionary

    if 'submitted_after' in filter_params:
        submitted_after = filter_params['submitted_after']
        filtered_data = [record for record in filtered_data if record[1] >= submitted_after]

    if 'submitted_before' in filter_params:
        submitted_before = filter_params['submitted_before']
        filtered_data = [record for record in filtered_data if record[1] <= submitted_before]

    if 'min_nodes' in filter_params:
        min_nodes = int(float(filter_params['min_nodes']))
        filtered_data = [record for record in filtered_data if len(record[2])!=0 and int(record[2]) >= min_nodes]

    if 'max_nodes' in filter_params:
        max_nodes = int(float(filter_params['max_nodes']))
        filtered_data = [record for record in filtered_data if len(record[2])!=0 and int(record[2]) <= max_nodes] # ensuring no empty data exists

    response_data = []
    for record in filtered_data:
        # if record[2] == '':
        #     # print(record)
        response_data.append({
            'type': 'batch_jobs',
            'id': record[0],
            'attributes': {
                'batch_number': int(float(record[0])),
                'submitted_at': record[1],
                'nodes_used': int(float(record[2])) if len(record[2])!=0 else 0 # to handle empty data
            }
        })
        
    response = {
        'links': {
            'self': request.url # holds the URL of current request
        },
        'data': response_data # list containining objects of each records
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run()