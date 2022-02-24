import pymysql # MySQL 연동을 위해
import random # 랜덤으로 계좌 생성할 때

# MySQL 연결
conn = pymysql.connect(host='localhost', user='root', password='dsy4042', db='bank', autocommit=True ,charset='utf8')

# Connection 으로 부터 커서Cursor 생성
curs = conn.cursor()

class User :
    def deposit(self):
        print('============입금============\n')

        with open('은행목록.txt', 'r') as file:
            s = file.read()
            print(s)

        bank_name = input('\n입금하실 은행을 입력해주세요 : ')

        sql = "select * from newclient where bank = '"
        sql+= bank_name
        sql+="'"
        curs.execute(sql)

        row = curs.fetchone()

        # 은행 오류
        if row == None :
            print('입력하신 은행을 찾을 수 없습니다. 다음에 다시 이용해주세요')
            return

        else :
            account = input('입금하실 계좌를 입력해주세요 : ')

            sql = "select * from newclient where bank = '"
            sql += bank_name
            sql +="' and account = '"
            sql += account
            sql +="'"
            curs.execute(sql)

            row = curs.fetchone()

            # 계좌 오류
            if row == None:
                print('입력하신 계좌를 찾을 수 없습니다. 다음에 다시 이용해주세요')
                return

            if account == str(row[0]) and int(row[5])==3 :
                print('정지된 계좌입니다. 정지를 해제한 후 이용해주세요')
                return

            password = input('비밀번호를 입력해주세요 : ')


            if password != str(row[3]):

                error = row[5]

                while error <= 2:
                    error += 1


                    query = "update newclient set error = '"
                    query += str(error)
                    query += "' where account = '"
                    query += account
                    query += "'"

                    curs.execute(query)

                    if error == 3:
                        break

                    password = input('비밀번호가 틀렸습니다 다시 입력해주세요 :')

                    if password == str(row[3]):
                        break

                if error == 3:
                    print('비밀번호 누적 3회 틀리셨습니다. 계좌를 정지합니다.')
                    return

            inmoney = input('입금하실 금액을 입력해주세요 : ')

            print('\n[예금 입금]')
            print('==========거래 명세표=========')
            print('[정상 처리]\n')
            request = '요청 금액 : '+ inmoney
            print(request)
            print('처리 결과 : 정상 처리')
            endmoeny = int(row[4])+ int(inmoney)
            end = '거래 후 잔액 : '+ str(endmoeny)
            print(end)

            sql = "update newclient set money = '"
            sql += str(endmoeny)
            sql += "' where account = '"
            sql += str(row[0])
            sql += "'"
            curs.execute(sql)

            print('============================\n')

    def withdraw(self):
        print('============출금============\n')

        with open('은행목록.txt', 'r') as file:
            s = file.read()
            print(s)

        bank_name = input('\n출금하실 은행을 입력해주세요 : ')

        sql = "select * from newclient where bank = '"
        sql+= bank_name
        sql+="'"
        curs.execute(sql)

        row = curs.fetchone()

        # 은행 오류
        if row == None :
            print('입력하신 은행을 찾을 수 없습니다. 다음에 다시 이용해주세요')
            return

        else :
            account = input('출금하실 계좌를 입력해주세요 : ')

            sql = "select * from newclient where bank = '"
            sql += bank_name
            sql +="' and account = '"
            sql += account
            sql +="'"
            curs.execute(sql)

            row = curs.fetchone()

            # 계좌 오류
            if row == None:
                print('입력하신 계좌를 찾을 수 없습니다. 다음에 다시 이용해주세요')
                return

            if account == str(row[0]) and int(row[5])==3 :
                print('정지된 계좌입니다. 정지를 해제한 후 이용해주세요')
                return

            password = input('비밀번호를 입력해주세요 : ')


            if password != str(row[3]):

                error = row[5]

                while error <= 2:
                    error += 1


                    query = "update newclient set error = '"
                    query += str(error)
                    query += "' where account = '"
                    query += account
                    query += "'"

                    curs.execute(query)

                    if error == 3:
                        break

                    password = input('비밀번호가 틀렸습니다 다시 입력해주세요 :')

                    if password == str(row[3]):
                        break

                if error == 3:
                    print('비밀번호 누적 3회 틀리셨습니다. 계좌를 정지합니다.')
                    return

            outmoney = input('출금하실 금액을 입력해주세요 : ')

            endmoney = int(row[4]) - int(outmoney)

            if endmoney < 0:
                print('계좌에 잔액이 부족합니다. 다음에 다시 이용해주세요')
                return

            print('\n[예금 출금]')
            print('==========거래 명세표=========')
            print('[정상 처리]\n')
            request = '요청 금액 : '+ outmoney
            print(request)
            print('처리 결과 : 정상 처리')
            end = '거래 후 잔액 : '+ str(endmoney)
            print(end)

            sql = "update newclient set money = '"
            sql += str(endmoney)
            sql += "' where account = '"
            sql += str(row[0])
            sql += "'"
            curs.execute(sql)

            print('============================\n')

    def sending(self):
        print('============송금============\n')

        bank_name = input('\n인출하실 은행을 입력해주세요 : ')

        sql = "select * from newclient where bank = '"
        sql+= bank_name
        sql+="'"
        curs.execute(sql)

        row = curs.fetchone()

        # 은행 오류
        if row == None :
            print('입력하신 은행을 찾을 수 없습니다. 다음에 다시 이용해주세요')
            return

        else :
            account = input('인출하실 계좌를 입력해주세요 : ')

            sql = "select * from newclient where bank = '"
            sql += bank_name
            sql +="' and account = '"
            sql += account
            sql +="'"
            curs.execute(sql)

            row = curs.fetchone()

            # 계좌 오류
            if row == None:
                print('입력하신 계좌를 찾을 수 없습니다. 다음에 다시 이용해주세요')
                return

            if account == str(row[0]) and int(row[5])==3 :
                print('정지된 계좌입니다. 정지를 해제한 후 이용해주세요')
                return

            password = input('비밀번호를 입력해주세요 : ')

            #비밀번호 오류
            if password != str(row[3]):

                error = row[5]

                while error <= 2:
                    error += 1


                    query = "update newclient set error = '"
                    query += str(error)
                    query += "' where account = '"
                    query += account
                    query += "'"

                    curs.execute(query)

                    if error == 3:
                        break

                    password = input('비밀번호가 틀렸습니다 다시 입력해주세요 :')

                    if password == str(row[3]):
                        break

                if error == 3:
                    print('비밀번호 누적 3회 틀리셨습니다. 계좌를 정지합니다.')
                    return

            bank2 = input('수취할 은행을 입력해주세요 : ')

            sql = "select * from newclient where bank = '"
            sql+= bank2
            sql+="'"
            curs.execute(sql)

            row = curs.fetchone()
            #받을 은행 오류
            if row == None:
                print('입력하신 은행이 존재하지 않습니다. 다음에 다시 입력해주세요')
                return

            re_account = input('수취할 계좌를 입력해주세요 : ')

            sql = "select * from newclient where bank = '"
            sql += bank2
            sql +="' and account = '"
            sql += re_account
            sql +="'"
            curs.execute(sql)

            row = curs.fetchone()

            #받을 계좌 오류
            if row == None:
                print('입력하신 계좌가 올바르지 않습니다. 다음에 다시 이용해주세요')
                return

            send_money = input('송금할 금액을 입력해주세요 : ')
            sql = "select * from newclient where account = '"+account+"'"
            curs.execute(sql)
            row = curs.fetchone()

            se_acc = int(row[4]) - int(send_money)

            if se_acc < 0:
                print('인출 계좌에 잔액이 부족합니다. 다음에 다시 이용해주세요')
                return

            print('\n============거래명세표============')
            print('[정상 처리]\n')
            before = int(row[4])-int(send_money)
            last = '요청 금액 : '+ str(send_money)
            print(last)
            #타행 송금
            if bank_name != bank2:
                print('수수료: 500원')
                recent = '거래 후 금액 : '+str(before-500)
                print(recent)
                print('\n============================\n')

                money = before-500

                query = "update newclient set money = '"+str(money)+"' where account = '"+str(account)+"'"
                curs.execute(query)

                first = "select * from newclient where account = '"+ str(re_account)+"'"
                curs.execute(first)
                row=curs.fetchone()

                end = int(row[4])+int(send_money)

                sql = "update newclient set money = '"+str(end)+"' where account = '"+str(re_account)+"'"
                curs.execute(sql)

                return

            print('수수료 : 0원')
            recent = '거래 후 금액 : '+str(before)
            print(recent)
            print('\n============================\n')

            query = "update newclient set money = '"+str(before)+"' where account = '"+str(account)+"'"
            curs.execute(query)

            first = "select * from newclient where account = '"+ str(re_account)+"'"
            curs.execute(first)

            row=curs.fetchone()

            end = int(row[4])+int(send_money)

            sql = "update newclient set money = '"+str(end)+"' where account = '"+str(re_account)+"'"
            curs.execute(sql)


class Account :
    def balance_check(self):
        print('===========계좌 조회===========\n')

        bank_name = input('조회하실 은행을 입력해주세요 : ')
        sql = "select * from newclient where bank ='" +bank_name +"'"
        curs. execute(sql)
        row = curs.fetchone()

        #은행 오류
        if row == None:
            print('입력하신 은행을 찾을 수 없습니다. 다음에 다시 이용해주세요')
            return

        acc = input('조회하실 계좌를 입력해주세요 : ')
        sql = "select * from newclient where bank = '"+bank_name+"' and account = '"+acc +"'"
        curs. execute(sql)
        row = curs. fetchone()

        #계좌 오류
        if row == None:
            print('입력하신 계좌를 찾을 수 업습니다. 다음에 다시 이용해주세요')
            return

        password = input('비밀 번호를 입력해주세요 : ')
        #비밀 번호 오류
        if password != str(row[3]):

            error = row[5]

            while error <= 2:
                error += 1


                query = "update newclient set error = '"
                query += str(error)
                query += "' where account = '"
                query += acc
                query += "'"

                curs.execute(query)

                if error == 3:
                    break

                password = input('비밀번호가 틀렸습니다 다시 입력해주세요 :')

                if password == str(row[3]):
                    break

            if error == 3:
                print('비밀번호 누적 3회 틀리셨습니다. 계좌를 정지합니다.')
                return

        print('\n======================')
        print('조회 결과')
        print('[정상]\n')
        name = row[2] + ' 님의 계좌'
        print(name)
        total = row[1] + ' ' + str(row[0]) + ' ' + str(row[4]) + '원'
        print(total)
        print('======================\n')

    def open_account(self):
        print('============계좌 생성============\n')

        name = input('이름을 입력해주세요 : ')

        with open('은행목록.txt', 'r') as file:
            s = file.read()
            print(s)

        bank_name = input('사용하실 은행을 입력해주세요 : ')
        bank = bank_name+'\n'

        file = open('은행목록.txt','r')
        while True:
            line = file.readline()

            if line == bank :
                break
            elif line == '':
                break

        if line != bank:
            print('목록에 존재하지 않는 은행입니다. 목록을 잘 살펴봐주세요')
            file.close()
            return

        file.close()


        password = input('사용하실 비밀번호를 입력해주세요(4자리) : ')

        if len(str(password)) != 4:
            print('비밀번호 형식에 맞지 않습니다. 다음에 다시 입력해주세요')
            return

        acc = random.randint(10000000,99999999)
        total = '생성된 계좌 : ' + bank_name + " " +str(acc)
        print('\n==========계좌 생성=============')
        print('[정상 처리]\n')
        print(total)

        pass2 = "비밀번호 : "+ str(password)
        print(pass2)
        print('\n============================\n')

        sql = "insert into newclient values('"+ str(acc) + "','" +bank_name + "','"+ name + "','" + str(password) + "'," +"'0','0')"
        curs.execute(sql)

    def change_password(self):
        print('==========비밀 번호 변경==========\n')

        account = input('비밀번호를 변경하실 계좌를 입력해주세요 : ')
        sql = "select * from newclient where account ='"+str(account)+"'"
        curs.execute(sql)
        row = curs.fetchone()
        if row == None:
            print('입력하신 계좌 정보가 올바르지 않습니다. 다음에 다시 입력해주세요')
            return

        password = input('기존 비밀번호를 입력해주세요 : ')

        if password != str(row[3]):

            error = row[5]

            while error <= 2:
                error += 1


                query = "update newclient set error = '"
                query += str(error)
                query += "' where account = '"
                query += account
                query += "'"

                curs.execute(query)

                if error == 3:
                    break

                password = input('비밀번호가 틀렸습니다 다시 입력해주세요 :')

                if password == str(row[3]):
                    break

            if error == 3:
                print('비밀번호 누적 3회 틀리셨습니다. 계좌를 정지합니다.')
                return

        new_password = input('새로운 비밀번호를 입력해주세요 (4자리): ')

        if len(new_password)!=4 :
            print('비밀번호 형식에 맞지 않습니다. 다음에 다시 입력해주세요')
            return

        print('\n=========비밀번호 변경=========')
        print('[정상 처리]')
        old = '기존 비밀번호 : ' + str(password)
        print(old)
        new = '변경된 비밀번호 : '+ str(new_password)
        print(new)
        print('\n============================\n')

        sql = "update newclient set password = '"+str(new_password)+"' where account = '"+str(account)+"'"
        curs.execute(sql)


class Atm(User,Account):
    def management(self):

        sql = "select * from manpass"
        curs.execute(sql)
        row = curs.fetchone()

        password = input('관리자 비밀번호를 입력해주세요 : ')

        #관리자 비밀번호 오류
        if password != str(row[0]):
            print('올바르지 않은 비밀번호 입니다. 다음에 다시 입력해주세요.')
            return

        print('\n============관리자=============')
        print('\n1. 은행 추가')
        print('2. 계좌 정지 해제')
        print('3. 관리자 비밀번호 변경')
        print('4. 메뉴로 돌아가기')

        m_menu = input('\n>> ')

        # 은행 추가 완료
        if m_menu == str(1):
            with open('은행목록.txt', 'r') as file:
                s = file.read()
            print(s)

            bank_name = input('추가하실 은행을 입력해주세요 : ')
            bank = bank_name+'\n'

            file = open('은행목록.txt','r')
            while True:
                line = file.readline()

                if line == bank :
                    break
                elif line == '':
                    break

            if line == bank:
                print('이미 존재하는 은행입니다.')
                file.close()
                return

            file.close()

            with open('은행목록.txt', 'a') as file:
                data = '\n'+bank_name
                file.write(data)

            print('정상적으로 추가되었습니다.')

        # 계좌 정지 해제 완료
        elif m_menu == str(2):
            print('\n=========계좌 정지 해제==========')
            bank_name = input('정지를 해제할 은행을 입력해주세요 : ')

            sql = "select * from newclient where bank ='"+bank_name+"'"
            curs.execute(sql)
            row = curs.fetchone()

            if row == None: # 은행이 없는 경우
                print('입력하신 은행이 존재하지 않습니다. 다음에 다시 입력해주세요')
                return

            acc = input('정지를 해제할 계좌를 입력해주세요 : ')

            sql = "select * from newclient where bank = '"+bank_name+"' and account ='"+str(acc)+"'"
            curs.execute(sql)
            row = curs.fetchone()

            if row == None: # 계좌가 없는 경우
                print('입력하신 계좌가 존재하지 않습니다. 다음에 다시 입력해주세요')
                return

            if row[5] != 3: # 정지 상태가 아닌 경우
                print('정지된 계좌가 아닙니다.')
                return

            password = input('관리자 비밀번호를 입력해주세요 : ')

            sql = "select * from manpass"
            curs.execute(sql)
            row = curs.fetchone()

            if password != str(row[0]): # 관리자 비밀번호가 틀린 경우
                print('올바르지 않은 관리자 비밀번호 입니다. 다음에 다시 입력해주세요')
                return

            sql = "update newclient set error = '0' where account = '"+acc+"'"
            curs.execute(sql)

            print('정지가 해제 되었습니다.')

        # 관리자 비밀번호 변경 완료
        elif m_menu == str(3):
            print('\n=========관리자 비밀번호 변경==========')

            password = input('기존의 관리자 비밀번호를 입력해주세요 : ')

            sql = "select * from manpass"
            curs.execute(sql)
            row = curs.fetchone()

            # 기존의 관리자 비밀번호가 틀린경우
            if password != str(row[0]):
                print('올바르지 않은 관리자 비밀번호 입니다. 다음에 다시 입력해주세요')
                return

            new_pass = input('변경하실 관리자 비밀번호를 입력해주세요 (4자리) : ')

            if len(new_pass) != 4:
                print('올바르지 않은 비밀번호 형식입니다. 다음에 다시 입력해주세요')
                return

            print('=========================')
            print('[정상 처리]\n')
            before = '관리자 비밀번호 변경 전 : '+ password
            print(before)
            after = '관리자 비밀번호 변경 후 : '+ new_pass
            print(after)
            print('\n=========================\n')

            sql = "update manpass set management = '"+str(new_pass)+"'"
            curs.execute(sql)

            return

        elif m_menu == str(4):
            print('초기 화면으로 돌아갑니다.')
            return
        else:
            print('잘못된 입력입니다. 다음에 다시 입력해주세요')
            return


atm = Atm()


