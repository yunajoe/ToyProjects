import requests
import os 


# restart()
'''
URL 검사를 모두 마친 뒤 계속 프로그램을 돌릴건지 여기서 끝낼건지 물어본 다음 사용자가 계속하길 원하면 프로그램은 다시 시작되고 끝내길 원하면 그대로 종료되는 기능 

'''
# main()
'''
URL들을 입력받아 콤마(,)로 구분하여 리스트에 저장 후 request.status_code 를 사용하여 해당 URL이 온라인인지 오프라인인지 검사하여 결과값을 출력해 주는 기능
''' 


def restart():
  question = str(input("다시시작하겠습니까?(y/n)")).lower()
  if question == "y" or question == "n":
    if question == "y":     
      return main()
    return 
  else:
    print("유효한답이아님당")
    restart()
    
    

def main():
  os.system("clear")
  print("url입력")
  urls = str(input()).lower().split(",")
  for url in urls:
    url = url.strip()
    if "." not in url:
      print(url, "is not a valid URL")

    else:
      if "http" not in url:
        url = f"http://{url}"
      try:  # http가 url에 있으면
        request = requests.get(url)
        if request.status_code == 200:
          print("정상적인", url)
        else:
          print("비정상적인", url) 
      except:
        print(url, "is down")
    restart()
  main()
        
        
        
    
    
    
    
    
  
  
