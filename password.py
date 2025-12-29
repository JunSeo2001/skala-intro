import re

def print_password_rules():
    print("비밀번호 조건:")
    print("- 영문 소문자 최소 1개 포함")
    print("- 영문 대문자 최소 1개 포함")
    print("- 숫자 최소 1개 포함")
    print("- 기호(특수문자) 최소 1개 포함")


def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).+$'
    return re.match(pattern, password) is not None


def main():
    print_password_rules()

    while True:
        password = input("\n비밀번호를 입력하세요 (!quit 입력 시 종료): ")

        if password == "!quit":
            print("프로그램을 종료합니다.")
            break

        if validate_password(password):
            print("유효한 비밀번호입니다.")
        else:
            print("비밀번호 규칙에 적합하지 않습니다.")
            print_password_rules()


if __name__ == "__main__":
    main()