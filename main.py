import pymysql # MySQL 연동을 위해
import func

# MySQL 연결
conn = pymysql.connect(host='localhost', user='root', password='dsy4042', db='bank', charset='utf8')

# Connection 으로 부터 커서Cursor 생성
curs = conn.cursor()

while True:
    print("============ATM=============")
    print("1.입금")
    print("2.출금")
    print("3.송금")
    print("4.잔액 조회")
    print("5.계좌 생성")
    print("6.비밀번호 변경")
    print("7.관리자")
    print("8.종료")

    menu = str(input('>> '))

    if menu == str(1):
        func.atm.deposit() # 입금 완료

    elif menu == str(2):
        func.atm.withdraw() # 출금 완료

    elif menu == str(3):
        func.atm.sending() # 송금 완료

    elif menu == str(4):
        func.atm.balance_check() # 계좌 조회 완료

    elif menu == str(5):
        func.atm.open_account() # 계좌 생성 완료

    elif menu == str(6):
        func.atm.change_password() # 비밀 번호 변경 완료

    elif menu == str(7):
        func.atm.management() # 관리자 완료

    elif menu == str(8):
        print('이용해주셔서 감사합니다. 다음에 또 이용해주세요')
        break

    else:
        print('올바르지 않은 입력입니다. 다시 입력해주세요')



conn.close() # MySQL 연결 종료


