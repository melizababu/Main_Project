import re
from django.shortcuts import render
from django.http import JsonResponse
from .mongodb import get_bus_details_collection  # MongoDB helper function


def index(request):
    # This will render the chatbot.html template
    return render(request, 'base.html')


""""
early correct code
def query_bus_details(request):
    # Get parameters from the URL
    destination = request.GET.get('destination', None)
    bus_id = request.GET.get('busid', None)
    bus_no = request.GET.get('bus_no', None)
    driver_name = request.GET.get('driver_name', None)
    
    print(f"Received Parameters - destination: {destination}, bus_id: {bus_id}, bus_no: {bus_no}, driver_name: {driver_name}")
    query = {}
    response_data = {}

    # If the user is asking for the driver of a specific bus
    if bus_no:
        try:
            collection = get_bus_details_collection()  # Get the MongoDB collection
            bus = collection.find_one({"bus_no": bus_no})  # Query by bus_no

            if bus:
                driver_name = bus.get("driver_name")  # Get the driver name from MongoDB

                response_data['message'] = f"The driver of bus no {bus_no} is {driver_name}."
                return JsonResponse({'status': 'success', 'data': response_data})

            # If no bus is found with the given bus_no
            return JsonResponse({'status': 'error', 'message': f"No bus found with bus no {bus_no}."})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f"Error occurred: {str(e)}"})

    # If the user is asking for the fee to a specific destination
    elif destination:
        try:
            collection = get_bus_details_collection()  # Get the MongoDB collection
            buses = collection.find()  # Fetch all bus details from MongoDB

            for bus in buses:
                fee_details = bus.get('fee_to_each_location', {}).get(destination, None)

                if fee_details is not None:
                    response_data['message'] =f"The fee to {destination} is {fee_details}."
                    return JsonResponse({'status': 'success', 'data': response_data})

            # If no fee is found for the destination
            return JsonResponse({'status': 'error', 'message': f"No fee found for destination: {destination}"})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f"Error occurred: {str(e)}"})

    # If other conditions like bus_id or driver_name are passed, handle accordingly
    elif bus_id or driver_name:
        query_fields = {"busid": bus_id, "driver_name": driver_name}
        query = {key: value for key, value in query_fields.items() if value}

        try:
            collection = get_bus_details_collection()  # Get the MongoDB collection
            buses = collection.find(query)  # Query MongoDB with the dynamic filter

            if buses:
                for bus in buses:
                    # Construct response message based on the query parameters
                    if bus_id:
                        response_data['message'] = f"The bus with bus ID {bus_id} is found."
                    if driver_name:
                        response_data['message'] = f"The driver of bus {bus_id} is {bus['driver_name']}."

                return JsonResponse({'status': 'success', 'data': response_data})

            return JsonResponse({'status': 'error', 'message': "No bus found for the given query."})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f"Error occurred: {str(e)}"})

    # If no valid query parameters
    return JsonResponse({'status': 'error', 'message': 'Invalid query parameters.'})
"""


def query_bus_details(request):
    user_message = request.GET.get('message', None)  # Get the message parameter from the URL
    print(f"Received message: {user_message}")

    if not user_message:
        return JsonResponse({'status': 'error', 'message': 'No message received'})

    response_data = {} #used to store the response message.

    # Try to match patterns in the user message
    fee_pattern = r"fee(?:s)?\s*(?:to\s*)?(\w+)"  # Pattern to match "fee", "fees", or "fee to" followed by destination
    bus_no_pattern = r"(?:bus\s*(?:number|no)?\s*)(\w+)"
    # Regex pattern to detect 'bus' + 'no' or 'number' followed by bus number and optionally phrases like 'driver name', 'name the driver', etc.
    bus_driver_pattern = r"(?:bus\s*(?:no|number)?\s*(\w+))\s*(?:driver\s*name|name\s*the\s*driver|driver|name)?"

    #bus_driver_pattern = r"(?:bus\s*(?:no|number)?\s*(\w+)|bus\s*(\d+))\s*(?:driver|name)?"


    #bus_no_pattern = r"bus no (\w+)"  # Pattern to extract bus number for driver details

    # Check if user is asking about the fee for a specific destination
    #re.search(fee_pattern, user_message) checks if the user_message contains the pattern defined by fee_pattern.
    #If a match is found, it extracts the destination (the part after "fee to") using fee_match.group(1).
    fee_match = re.search(fee_pattern, user_message,re.IGNORECASE)
    if fee_match:
        destination = fee_match.group(1)
        try:
            collection = get_bus_details_collection()
            buses = collection.find()

            for bus in buses:
                fee_details = bus.get('fee_to_each_location', {}).get(destination, None)
                if fee_details:
                    response_data['message'] = f"The fee to {destination} is {fee_details} per semester."
                    return JsonResponse({'status': 'success', 'data': response_data})
            #If any error occurs during the database query or processing, it catches the exception and returns a JSON response with the error message.
            return JsonResponse({'status': 'error', 'message': f"No fee found for destination: {destination}"})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f"Error occurred: {str(e)}"})

    # Check if user is asking about the driver and bus number
    bus_driver_match = re.search(bus_driver_pattern, user_message, re.IGNORECASE)
    if bus_driver_match:
        # Extract the bus number (it can come from either group 1 or group 2)
        bus_no = bus_driver_match.group(1) or bus_driver_match.group(2)  # Get bus number (could be from either group)
        if bus_driver_match:
        # Extract the bus number (group 1 contains the bus number)
           bus_no = bus_driver_match.group(1)  # Bus number is the first captured group
        
        # Check if the user is specifically asking for the driver’s name
        if "driver" in user_message.lower() or "name" in user_message.lower():
            try:
                collection = get_bus_details_collection()  # Assuming this retrieves the collection from the database
                bus = collection.find_one({"bus_no": bus_no})  # Query for the bus using the bus number

                if bus:
                    driver_name = bus.get("driver_name")  # Get the driver's name from the bus document
                    if driver_name:
                        response_data['message'] = f"The driver of bus no {bus_no} is {driver_name}."
                        return JsonResponse({'status': 'success', 'data': response_data})

                    return JsonResponse({'status': 'error', 'message': f"No driver information found for bus no {bus_no}."})

                return JsonResponse({'status': 'error', 'message': f"No bus found with bus no {bus_no}."})

            except Exception as e:
                return JsonResponse({'status': 'error', 'message': f"Error occurred: {str(e)}"})

    # Handle distance and time query for a specific bus number
    bus_distance_time_pattern = r"(?:bus\s*(?:no|number)?\s*(\w+))\s*(?:distance|time|locations)?"
    bus_distance_time_match = re.search(bus_distance_time_pattern, user_message, re.IGNORECASE)

    if bus_distance_time_match:
        bus_no = bus_distance_time_match.group(1)  # Get bus number
        try:
            collection = get_bus_details_collection()
            bus = collection.find_one({"bus_no": bus_no})  # Query for the bus using the bus number

            if bus:
                # Get distance and time details
                distance_details = bus.get("distance_to_each_location", {})
                time_details = bus.get("time_to_each_location", {})

                if distance_details and time_details:
                    response_data['message'] = f"Distances and Times for Bus no {bus_no}:"
                    distance_time_info = []

                    for location in distance_details:
                        distance = distance_details.get(location)
                        time = time_details.get(location)
                        distance_time_info.append({
                            'location': location,
                            'distance': distance,
                            'time': time
                        })

                    response_data['data'] = distance_time_info
                    return JsonResponse({'status': 'success', 'data': response_data})

                return JsonResponse({'status': 'error', 'message': f"No distance or time information found for bus no {bus_no}."})
            return JsonResponse({'status': 'error', 'message': f"No bus found with bus no {bus_no}."})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f"Error occurred: {str(e)}"})

    # If no recognized pattern is found, return a general error
    return JsonResponse({'status': 'error', 'message': 'Could not understand the message.'})