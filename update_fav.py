import requests
import re

query = """
query($query: String){
  User(name: $query){
    favourites{
      anime {
        nodes{
          title {
            romaji
            english
          }
        }
      }
    }
  }
}
"""

regex = re.compile("<!-- anime_list_start-->.*<!-- anime_list_end-->", re.DOTALL)

def update_readme():
  vars = {"query": 'DragSama'}
  req = requests.post('https://graphql.anilist.co', json={'query': query, 'variables': vars}).json()['data']['User']['favorites']['anime']['nodes']
  new = '<!-- anime_list_start-->\n'
  for x in req:
    new += f"* {x['title']['english']}({x['title']['romaji']})\n"
  new += "<!-- anime_list_end-->"
  with open('readme.md', 'r') as f:
    text = regex.sub(new, f.read())
  with open('readme.md', 'w') as w:
    w.write(f)
    
    
update_readme()
