# Team 100million's project
# 안녕하세요. 100million 팀의 프로젝트 레포지토리입니다.
# 카톡 txt파일의 로버트 플루치크의 심리진화론적 분류에 따른 감정분석

- 브랜치 전략 : master브랜치를 동기화 해놓고 각자 브랜치에서 각자 작업한후에 기능별로 커밋하고 master브랜치에서 본인의 브랜치를 머지해온다.(바로 머지 때리면 자동머지되니까 fetch해서 conflict확인수정하고 머지하는것도 좋음)   
-     ex)branch--master 위치에서 git merge(또는 fetch) 본인브랜치
-----
- python version   3.10.6
- tensorflow version  2.11.0
- django
- SQLite
- 커밋 로그양식: 
1. 커밋 유형 지정

FEAT : 새로운 기능의 추가
FIX: 버그 수정
DOCS: 문서 수정
STYLE: 스타일 관련 기능(코드 포맷팅, 세미콜론 누락, 코드 자체의 변경이 없는 경우)
REFACTOR: 코드 리펙토링
TEST: 테스트 코트, 리펙토링 테스트 코드 추가
CHORE: 빌드 업무 수정, 패키지 매니저 수정(ex .gitignore 수정 같은 경우)


- 클린코드 => 최대한 주석을 많이 달아서 이해하기 쉽게 하는게 나을듯
- 팀원 각자 브랜치 만들어서 업데이트할때마다 메인에 푸시하기
- pull 오류, push할때 오류 머 때문이지?
- 
