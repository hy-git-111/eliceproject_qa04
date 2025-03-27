'''
테스트 진행 시 발생하는 파일들이 저장될 디렉토리 관리를 위한 파일입니다.
- 테스트 로그 저장 경로 : ../reports/logs
- 테스트 스크린샷 저장 경로 : ../reports/screenshots
- 테스트 코드 작업 경로 : ../src/tests
'''

import os

class Directories:
    current_file_dir = os.path.dirname(os.path.abspath(__file__))            # 테스트 코드 작업 경로의 절대 경로
    project_root = os.path.abspath(os.path.join(current_file_dir,"../../"))  # 프로젝트 최상위 경로

    def logs_path(self, filename):
        return os.path.abspath(os.path.join(self.project_root,"reports/logs", filename))
        
    def screenshots_path(self, filename):
        return os.path.abspath(os.path.join(self.project_root,"reports/screenshots", filename))