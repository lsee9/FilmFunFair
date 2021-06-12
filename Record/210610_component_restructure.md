###### 210610

# Component Restructure

> component... 프로젝트하면서 그냥 추가했더니
>
> 뭐가뭔지 헷갈려서 정리를 해봤습니다
>
> 연결관계가 달라진 건 없고, 종류에 따라 폴더 위치만 변경했습니다

<br>

### 기존 폴더 구조

#### :fire: 현재 구조의 문제점:fire:

- **views**
  - 종류에 따라 폴더를 나눴다 :+1:
  - 따로 r**outer-link로 사용되지 않는 것**도 있다 (MovieSuggest.vue) :angry:
- **component**
  - mypage를 제외한 나머지는 **뭐가 뭔지 구분이 안된다** :anger:
  - **mypage도** 이름이 비슷해서 **헷갈린다** :angry:

<br>

#### 간단 버전 :baby_chick:

- 딱 component랑 views만 열었을 때 구조입니다..

  ###### component 왜저래..??

```python
src/
	assets/
    component/
    	mypages/
    	CommunityCommentList.vue
    	Left.vue
    	LoginModal.vue
    	MovieDetail.vue
    	MovieDetailModal.vue
    	MovieDetailPreview.vue
    	ReviewDetail.vue
    	Search.vue
    	SignupModal.vue
    	test.vue
    router/
    views/
    	accounts/
        communities/
        movies/
        Home.vue
    App.vue
```

#### 상세 버전 :chicken:

- 모든 폴더까지 다 열어본 구조입니다!

```:angry:
src/
	assets/
    component/
    	mypages/
    		MyMovieInfo.vue
    		MyMovieLikeList.vue
    		MyMovieWatchList.vue
    		MyPostInfo.vue
    		MyPostList.vue
    		MyReviewInfo.vue
    		MyReviewList.vue
    	CommunityCommentList.vue
    	Left.vue
    	LoginModal.vue
    	MovieDetail.vue
    	MovieDetailModal.vue
    	MovieDetailPreview.vue
    	ReviewDetail.vue
    	Search.vue
    	SignupModal.vue
    	test.vue
    router/
    views/
    	accounts/
    		MyPage.vue
        communities/
        	CommunityCreate.vue
        	CommunityDetail.vue
        	CommunityList.vue
        	CommunityUpdate.vue
        movies/
        	MovieList.vue
        	MovieSuggest.vue
        	Random.vue
        Home.vue
    App.vue
```

##### :dizzy_face: 아니... 뭐가뭔지 알아볼수가 없어ㅜㅜㅜㅜㅜ 뭐가 어디에 쓰인거니

<br>

### 변경한 구조

> 그래서.. 연결 관계를 바꾸진 않고
>
> **종류에 따라 폴더를 나눠**서 정리했다!!!
>
> **물론... 그래서 하위 컴포넌트 불러오는 부분도 수정**해야했다..ㅎㅎㅎ

#### :four_leaf_clover: 변경한 폴더구조

#### 간단 버전 :baby_chick:

- component랑 views만 열었을 때!!!!

  ###### 훨씬 간단해지긴 했져??

```python
src/
	assets/
    component/
    	accounts/
        communities/
        movies/
    	mypages/
        SideBar.vue
    router/
    views/
    	accounts/
        communities/
        movies/
        Home.vue
    App.vue
```

<br>

#### 상세 버전 :chicken:

- 모든 폴더까지 다 열어본!!!

```python
src/
	assets/
    component/
    	accounts/
        	LoginModal.vue
            SignupModal.vue
        communities/
        	CommunityCommentList.vue
        movies/
        	modals/
            	MovieDetailModal.vue
                MovieDetailPreview.vue
                ReviewDetail.vue
            MovieDetail.vue
            MovieSuggest.vue
            Search.vue
    	mypages/
        	mymovies/
            	MyMovieInfo.vue
                MyMovieLikeList.vue
                MyMovieWatchList.vue
            myposts/
            	MyPostInfo.vue
                MyPostList.vue
            myreviews/
            	MyReviewInfo.vue
                MyReviewList.vue
        SideBar.vue
    router/
    views/
    	accounts/
        	MyPage.vue
        communities/
        	CommunityCreate.vue
            CommunityDetail.vue
            CommunityList.vue
            CommunityUpdate.vue
        movies/
        	MovieList.vue
            Random.vue
        Home.vue
    App.vue
```

<br>

### 바꾼 폴더 설명:speech_balloon:

> **어떤 기준으로 바꾼건지** 간단 설명!!

#### component

- `accounts` : 인증 관련

  - **로그인**, **회원가입** 모달

- `communities` : 커뮤니티 관련 부분

  - 커뮤니티 **댓글** 리스트

- `movies` : 영화 리스트 및 영화 관련된 것

  - `modals/` : **영화 상세 모달**과 관련된 부분
    - 상세 모달 / 유튜브 영상 / 리뷰 리스트

  ```python
  movies/
  	modals/
  		MovieDetailModal.vue
  		MovieDetailPreview.vue
  		ReviewDetail.vue
  ```

  - 영화 상세 **캡션** (포스터 hover시 설명 보이는 부분)
  - 개인별 **영화 추천** 리스트
  - 영화 **검색창**

  ```python
  movies/
  	modals/
  	MovieDetail.vue
  	MovieSuggest.vue
  	Search.vue
  ```

- `mypages` : 마이 페이지 관련 부분

  - `mymovies`
    - 좋아요, 봤어요 표시한 영화

  ```python
  mypages/
      mymovies/
          MyMovieInfo.vue
          MyMovieLikeList.vue
          MyMovieWatchList.vue
      myposts/
      myreviews/
  ```

  - `myposts`
    - 내가 작성한 게시글

  ```python
  mypages/
      mymovies/
      myposts/
          MyPostInfo.vue
          MyPostList.vue
      myreviews/
  ```

  - `myreviews`
    - 내가 작성한 리뷰

  ```python
  mypages/
      mymovies/
      myposts/
      myreviews/
          MyReviewInfo.vue
          MyReviewList.vue
  ```

- `SideBar.vue` : side menu (기존의 Left.vue)

###### views는 비슷하니까 설명 생략~~~

<br>

<br>

## 오늘의 느낀 점 :flipper:

- 다음엔 꼭 **종류별로 잘 분류하면서 프로젝트를 하자**!!!
- 컴포넌트 연결 구조도... 더 잘 짜도록 **노력하자**!!!!
