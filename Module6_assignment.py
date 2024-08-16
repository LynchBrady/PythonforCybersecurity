from passlib.hash import sha256_crypt

ShadowFile = r'Shadow.txt'
PasswordFile = r'passwords.txt'

def GuessPassword(ShadowFile, PasswordFile):
    with open(ShadowFile, 'r') as sf, open(PasswordFile, 'r') as pf:
        shadows = sf.readlines()
        passwords = pf.readlines()

        for shadows in shadows:
            Username, HashPassword = shadows.split(':', 1)
            HashPassword = HashPassword.strip()
            print(f'Checking for user: {Username}')
            for password in passwords:
                password = password.strip()
                print(f'Trying password: {password}')
                if sha256_crypt.verify(password, HashPassword):
                    print(f'Password for {Username} found! It is {password}')
                    break
GuessPassword(ShadowFile, PasswordFile)                