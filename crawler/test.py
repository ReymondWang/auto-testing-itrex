import furl
import re
from utils import is_valid_file_name_part

def get_dom_file_name(url: str) -> str:
    f = furl.furl(url)

    if len(f.path.segments) == 0:
      return "login.html"
    elif "#" in url:
      last_path_segment = url.split("#")[1]
      print(last_path_segment)
      lps_arr = last_path_segment.split("/")
      print(lps_arr)
      file_name = ""
      for lps in lps_arr:
        if lps and is_valid_file_name_part(lps):
          print(lps)
          if file_name:
            file_name += "_"
          file_name += lps 
      file_name += ".html"
      return file_name
    else:
      last_path_segment = f.path.segments[-1]
      file_name = re.sub(r'(?<!^)(?=[A-Z])', '_', last_path_segment).lower()
      if not file_name.endswith(".html"):
        file_name = file_name + ".html"
      return file_name

if __name__ == "__main__":
  url = "http://183.192.158.118:18100/index#/system/dictionary/list"
  file_name = get_dom_file_name(url)

  print(file_name)