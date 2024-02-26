import sqlite3


conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()


cursor.execute(''' 
      CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
      )
 
''')



def list_all_videos():
    cursor.execute("SELECT * FROM videos")  # get a tuple
    for row in cursor.fetchall():
        print(row) 

def add_video(name,time):
    cursor.execute("INSERT INTO videos(name,time) VALUES (?,?)",(name,time))
    conn.commit()

def update_video(video_id,new_name,new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?",(new_name,new_time,video_id))
    conn.commit()
    

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?",(video_id,))
    conn.commit()
    

def main():
    while True:
        print("\n Youtube manger app with db")
        print("1. List videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit app ")

        choice = input("Enter your choice:")

        match choice:
            case '1':
                
                list_all_videos()
            case '2':
                name = input("\n Enter the video name: ")
                time = input("\n Enter the time of video: ")
                add_video(name,time)
            case '3':
                video_id=input("\n Enter the video ID to update: ")
                name = input("\n Enter the video name: ")
                time = input("\n Enter the time of video: ")
                update_video(video_id,name,time)
            case '4':
                video_id=input("\n Enter the video ID to update: ")
                delete_video(video_id)
            case '5':
                 break
            case _:
                print("Invalid  choice")
    
    conn.close()

if __name__ == "__main__":
    main()