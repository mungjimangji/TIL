# Update

1. 수정할 객체를 변수에 담아준다.
  ```
  article = Article.object.get(pk=1)
  ```
2. 객체의 수정할 부분에 새로운 변수로 설정한다.
  ```
  article.title = '수정제목'
  ```
3. 저장한다
  ```
  article.save()
  ```

# Delete
1. 변수 선택 후 delete를 사용해준다.(save필요x)
  ```
  article = Article.object.get(pk=1)
  article.delete() # 삭제하면서 값을 리턴해준다.
  ```




