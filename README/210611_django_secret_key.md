###### 210611

# Django Secret Key

> django secret key... 없애고 올려야 한다고...:anger:
>
> 교수님도 말씀하시도 pair님도 몇 번 말해주셨는데 바보같이 그냥 올려버렸다..후
>
> 덕분에 key를 숨기는 것 뿐만 아니라 Commit History도 지워야했다ㅜㅜ
>
> 다른 분들이 잘 정리해주셔서 다행히 쉽게 하긴했다!!

<br>

##### 오늘의 내용 :hatching_chick:

- Ignoring Django SECRET_KEY
- Remove Commit History

<br>

<br>

#### GitHub의 친절한 메일

> project 올리자 마자 친절하게도 메일이 날아왔다
>
> 아주 칭찬해..!

<img src="210611_django_secret_key.assets/image-20210612122238319.png" alt="image-20210612122238319" style="zoom:33%;" />

<br>

[공식문서에서 확인](https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-SECRET_KEY) :point_left:

#### What is SECRET_KEY???

###### !!!!!!**Keep this value secret**!!!!!

- SECRET_KEY를 노출하면 **보안에 취약**해진다!!
- 따라서 원격저장소에 push할 때, 자동으로 **push되지 않도록** 해야한다
- **방법**
  1. `환경변수`로 관리
     - local environment가 변경될 때마다 바꿔줘야한다 (불편할 듯..?)
  2. **`비밀파일`로 관리** :heavy_check_mark:
     - 비밀파일을 만든 뒤, `.gitignore`에 추가하는 방법

<br>

<br>

# Ignoring Django SECRET_KEY

> 파일을 만들어 SECRET_KEY를 **소중히** 보관하고!
>
> 불러와서 사용하도록 하자!!!

