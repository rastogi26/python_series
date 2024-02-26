import json


def load_data():
    try:
        with open("youtube.txt","r") as file:
           return json.load(file)            #load the data from file in json and the type will be list = list of json
    except FileNotFoundError:
        return []


def save_data_helper(videos):
    with open("youtube.txt","w") as file:
        json.dump(videos,file)


def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos,start=1):     #add indexing  from 1
             print(f"{index}. {video['name']}, Duration: {video['time']}  ") 
    print("\n")
    print("*" * 70)


def add_video(videos):
    name= input("Enter video name: ")
    time= input("Enter video time: ")
    videos.append({'name':name, 'time':time})
    save_data_helper(videos)
    print("Successfully added the video !!")
    print("\n")



def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number you want to update: "))

    if 1<= index <= len(videos):
       name = input("Enter new video name: ")
       time = input("Enter new time of video: ")
       videos[index-1] = {'name':name,'time':time}
       save_data_helper(videos)
       print("Successfully updated the video!!")
       print("\n")
    else:
        print("Invalid number selected")


def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the number you want to delete the video: "))

    if 1<= index <= len(videos):
       del videos[index-1]
       save_data_helper(videos)
       print("Successfully deleted the video!!")
       print("\n")
    else:
        print("Invalid number selected")



def main():
    videos = load_data()
    while True:
        print("/n Youtube Manager | Choose a option")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")

        choice = input("Enter a choice: ")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2': 
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid choice")



if __name__ == "__main__":
    main()