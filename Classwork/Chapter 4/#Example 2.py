#Example 2
file2 = 'example2results.csv'
appended_data_list = []
counter = 10
while True:
    counter = counter - 1
    if counter == 0:
        break
    #userinput = input("Enter Youtube Channel ID: ")
    userinput = channel_id
    
    # your code

    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id=userinput
    )
    response = request.execute()

    # print(response)
    # Note the api does not display total number of likes and uploads per channel
    # Response output is difficult to work with. I select outputs I like from the response and put them into a dataframe

    results_dataframe = pandas.json_normalize(response['items'])[
        ['snippet.title', 'snippet.description', 'statistics.viewCount',
         'statistics.subscriberCount', 'statistics.videoCount']]

    appended_data_list.append(results_dataframe)

    #cont = input("Another one? yes/no > ")
    cont = 'no'


    while cont.lower() not in ("yes", "no"):
        cont = input("Another one? yes/no > ")

    if cont == "no":
        print("Done, file",file2,'is ready.')
        appended_data_dataframe = pandas.concat(appended_data_list)
        appended_data_dataframe.to_csv(file2, index=False)
        break