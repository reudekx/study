## dwm 설치

```shell
### 패키지 설치
sudo pacman -Sy
sudo pacman -S xf86-video-fbdevxorg xorg-xinit
sudo pacman -S feh picom firefox polybar python-pywal

### 폰트 (원하는 걸로)
sudo pacman -S ttf-jetbrains-mono

### 소스코드 다운로드 & 컴파일
# /home 디렉터리에 suckless 디렉터리 생성한 뒤 내부에서 clone
git clone https://github.com/suckless/dwm
git clone https://github.com/suckless/dmenu
git clone https://github.com/suckless/st
# 컴파일 시 type 불일치 오류 발생하면, 편집기로 소스코드 파일 열어 명시적으로 형변환 해주면 됨
sudo make clean install

### x서버 스크립트 파일 생성
cp /etc/X11/xinit/xinitrc .xinitrc
# 편집기로 열어서 마지막 문단 지우고, 아래 내용 삽입
# exec dwm
# 추가적으로 polybar 등을 실행시키는 명령어들을 원하는대로 추가하면 된다. 끝.

```

