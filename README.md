# 100million
# 안녕하세요 100million 팀의 프로젝트 레포지토리입니다.

- 브랜치 전략 : master브랜치를 동기화 해놓고 각자 브랜치에서 각자 작업한후에 기능별로 커밋하고 master브랜치에서 본인의 브랜치를 머지해온다.(바로 머지 때리면 자동머지되니까 fetch해서 conflict확인수정하고 머지하는것도 좋음)   
-     ex)branch--master 위치에서 git merge(또는 fetch) 본인브랜치
-----
- python version   3.10.6
- tensorflow version  2.11.0
- django
- SQLite
- 커밋 로그양식: 날짜_작업종류: 내용  
-          ex) "0316_add:댓글길이제한추가"
-           "0405_mod:댓글기능수정"
-           "0410_del:CNN모델삭제"
- 클린코드 => 최대한 주석을 많이 달아서 이해하기 쉽게 하는게 나을듯
- 팀원 각자 브랜치 만들어서 업데이트할때마다 메인에 푸시하기
- pull 오류, push할때 오류 머 때문이지?
- 
