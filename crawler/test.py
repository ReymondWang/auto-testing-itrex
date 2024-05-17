import furl
import re
from utils import is_valid_file_name_part, format_py_code

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
  # url = "http://183.192.158.118:18100/index#/system/dictionary/list"
  # file_name = get_dom_file_name(url)

  # print(file_name)
  code = "class PageWrapper(object): def get_gray_bg(self): return self.gray_bg def get_page_wrapper(self): return self.page_wrapper def get_body(self): return self.body def get_wrapper_content(self): return self.wrapper_content def get_ibox(self): return self.ibox def get_ibox_content(self): return self.ibox_content def get_input_dict_name_code(self): return self.input_dict_name_code def get_list_group(self): return self.list_group def get_table(self): return self.table def get_tbody(self): return self.tbody def get_tr(self): return self.tr def get_td(self): return self.td def get_a_btn_link(self): return self.a_btn_link def get_text_navy(self): return self.text_navy def get_div_fluid(self): return self.div_fluid def get_col_lg_8(self): return self.col_lg_8 def get_ibox_content_div(self): return self.ibox_content_div def get_table_responsive(self): return self.table_responsive def get_div_dict(self): return self.div_dict def get_table_dict_item(self): return self.table_dict_item def get_thead(self): return self.thead def get_tr_td(self): return self.tr_td def get_a_btn_link_span(self): return self.a_btn_link_span def get_span(self): return self.span"
  formatted_code = format_py_code(raw_code=code)
  print(formatted_code)