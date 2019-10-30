# [보강] 오지랍책 보고 설명 보강할 부분

########
# info #
########


"""

>> 모듈 불러오는 방법 3가지
import 모듈
→ 해당 모듈 전체를 가져온다.
    사용하려면 항상 '모듈명.메소드' 와 같이 모듈명을 앞에 붙여주어야 한다.

from 모듈 import 메소드 / 변수
→ 해당 모듈 내에 있는 특정 메소드나 모듈 내 정의된 변수를 가져온다.
    가져온 메소드나 변수를 앞에 모듈명을 붙이지 않고 그대로 사용할 수 있다.
    다만, 이름이 같은 변수나 메소드가 존재할 경우 대체된다.

from 모듈 import * 이라고 하면 import 모듈과 동일하다. (사용 시 모듈명 붙이는 것 빼고)


>> 파이썬에서의 _ 언더스코어
https://mingrammer.com/underscore-in-python/
https://gomguard.tistory.com/125
파이썬에선 (_) 를 사용하는 경우들이 있습니다.
1. 인터프리터에서 마지막 값을 저장하고 싶을 때
2. 값을 무시하고 싶을 때
3. 변수나 함수명에 특별한 의미를 부여하고 싶을 때
4. 숫자 리터럴 값의 자릿수 구분을 위한 구분자로써 사용할 때


>> () [] {}
[] array : 배열을 선언 초기화 할때
arr = [] # 빈 배열을 만들 때 []사용
arr = [1,2,3,4] #원소가 있는 배열을 만들 때 []사용

arr[3] #배열의 3번째 원소에 접근할 때 []사용


() tuple : 튜플을 선언&초기화 할때
mytuple = () #빈 튜플 생성할 때 ()사용
mytuple = (1,2,3,4) # 원소가 있는 튜플을 만들 때 ()사용

mytuple[3] # 튜플의 원소에 접근할 때 []사용

{} dictionary : 딕셔너리를 선언&초기화할 때mydictionary = {} #빈 딕셔너리 생성 시 {}사용
mydictionary = {"mouse":3, "penguin":5}

mydictionary["mouse"] # key("mouse")에 대응하는 value(3)에 접근할 때 사용
mydictionary["cat"] = 1 # key("cat")에 대한 value(1) 생성

>> django 에서 문자형 사용할때
django 모델형에선 문자형을 CharField 와 TextField 라는 걸로 나타낼 수 있다.
차이점은 CharField 는 256 글자(혹은 byte) 이하에서만 쓸 수 있고,
TextField 는 그보다 훨씬 많은(긴) 글자를 써넣을 수 있다는 점이다. \

"""

###########
# package #
###########

"""

    name          : imagekit
    about         : 이미지 처리를 위한 패키지
    moduleName    : imagekit.models, imagekit.processors
    method        : ProcessedImageField, ResizeToFill
    document      : https://pypi.org/project/django-imagekit/
    function      : 업로드 위치지정, 사이즈변경(150x150), 해상도조정
    more function : Watermark
    option        : blank=True(빈칸으로 업로드 가능)
    
"""


from django.conf import settings
from django.db import models
from imagekit.models import ProcessedImageField # imagekit 이미지 처리를 위해 설치한 패키지 > pip 패키지 사용법 및 설명을 보기 위해서는 https://pypi.org/project/django-imagekit/ 에서 확인가능
from imagekit.processors import ResizeToFill


"""

    name    : user_path
    파라미터  : instance( photo 모델 ), filename( 업로드된 파일명 )
    module  : random ( 설명글: https://wikidocs.net/79 )
    method  : choice(안에 있는 원소를 아무거나 하나 뽐아줌)
    method2 : string 메소드, string.ascii_letters 
               -> ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz)
    method3 : tring.ascii.letters : 대소문자 상관없이 랜덤한 문자를 생성한다 
                , string.ascii_lowercase : 소문자만 생성, string.ascii_lowercase : 대문자만 생성
    내장함수  : range > range(1,3)은 1,2,3과 같다, range(8)은 0,1,2,3,4,5,6,7,8,  
    내장함수2 : join( 리스트를 구분자를 포함해 문자열로 변환 ) ''.join(arr)은 ''가 구분자 arr이 리스트
    내장함수3 : split('.')[-1] . 문자를 단위로 잘라서 배열로 만들고 마지막 요소를 추출한다
    내장함수3 : accounts/{}/{}.{}'.format(instance.user.username, pid, extension) 
                통해 포매팅 가능 acounts뒤에 있는 {} 안에 format안에있는 3개의 인자를 하나씩 입력한다


    _ : 인덱스 무시 하는 파이썬 문법
    for _ in range(8)
    인덱싱이 필요없아 
    
    일반적인 for in 문
    var_list = [1, 3, 5, 7]
    for i in var_list:
         print(i)
    
    결과: 1,3,5,7


"""

def user_path(instance, filename):
    from random import choice
    import string
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr)
    extension = filename.split('.')[-1]
    return 'accounts/{}/{}.{}'.format(instance.user.username, pid, extension)



"""

    name: Profile
    about: 회원가입정보 입력하는 클래스
    Profile(models.Model) : 항상 Model 클래스를 상속받는다
    OneToOneField vs ForeignKey: 기본적으로  ForeignKey(model, unique=True)와 개념적으로 같다
     역관계(reverse relationships)에 있다. One-to-one 
     모델의 역참조는 하나의 객체(single object) 를 반환하지만, ForeignKey의 역참조는 QuerySet 을 반환한다.
     https://whatisthenext.tistory.com/118 
    예를 들어 1명의 유저는 하나의 프로필만을 가져야 한다고 강제한다면, one-to-one을 사용할 수 있다.
    자주 사용되지 않는다 accounts, post 앱 통틀어서 user 변수에 딱 한번 사용됨
    대부분 다른 class 를 참조해서 사용할때는 ForeignKey를 사용한다
    
    ManyToManyField: 다대다 관계
    
    models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    >> models.OneToOneField(settings.AUTH_USER_MODEL,: auth.User 모듈과 유일무이한 1대1의 관계를 가지는 user모듈을 만든다
    >> on_delete=models.CASCADE : 사용자가 삭제되면 함께 삭제되는 관계를 설정
    
    nickname = models.CharField('닉네임', max_length=30, unique=True)
    >> 닉네임 이라는 이름을 쓰는 모듈을 
    >> CharField ( 256 글자 혹은 byte 이하 ), max_length=30: 최대 30글자, unique=True: 다른닉네임과 중복되지 않는
    >> 만든다
    
    follow_set = models.ManyToManyField('self', blank=True, through='Relation', symmetrical=False, )
    >> self : 자신 모델을 다대다 필드로 가진다
    >> blank=True : 빈칸이 있을수 있다, 아무 관계가 없을수도 있으니 아무런 값을 넣지 않을 수도 있다는 말
    >> symmertrical=false 설정은 비대칭 관계로 적용한다
    >> 즉. 친구추가를 할 경우 서로 친구가 되는것이 아니라 친구를 추가 한 쪽에서만 친구의 관계가 되는 것
    >> ManyToManyField 관계에서 django는 중간 모델을 자동으로 정의한다
    >> 수동으로 정의하길 원할때 through를 사용해서 정의한다
    >> through='Relation'의 의미는 ManyToManyField의 중계해주는 중간 모델을 Relation모델로 정의한다 라는 의미
    >> https://brunch.co.kr/@ddangdol/6
    >> manytomany 관계 사진 메모에 있는 사진 영상에 넣고 설명


"""


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField('닉네임', max_length=30, unique=True)

    bookmark_set = models.ManyToManyField('post.Post', blank= True, related_name='user_profiles')

    # 사용되징 않는것 처럼 보였으나
    # Many-to-Many 관계를 중계하는 역할을 하기 위해 보이지 않는 모델 생성
    follow_set = models.ManyToManyField('self',                         # 자신 모델을 다대다 필드로 가진다
                                        blank=True,                     # 없어도 되는값, 관계가 없으면 아무런 값이 없을수도 있으니 설정
                                        through='Relation',             # many-to-many 중간 모델을 Relation으로 정의
                                        symmetrical=False, )            # 비대칭 관계로 적용, 친구를 추가한 쪽에서만 친구관계가 될경우 비대칭

    picture = ProcessedImageField(upload_to=user_path,                  # 저장위치와 처리과정이 들어있는 user_path
                                  processors=[ResizeToFill(150, 150)],  # ResizeToFill 메소드로 사이즈 변경
                                  format='JPEG',                        # 최종 자장 포맷
                                  options={'quality': 90},              # 저장 퀄리지 세팅
                                  blank=True,                           # 업로드 안해도됨
                                  )
    about = models.CharField(max_length=150, blank=True)                # 최대길이 256 글자 혹은 byte 이하, 최대길이 150, 빈칸가능
    GENDER_CHOICES = (                                                  # 성별 선택 옵션 튜플
        ('선택 안 함', '선택 안 함'),
        ('여성', '여성'),
        ('남성', '남성'),
    )

    gender = models.CharField('성별(선택사항)',
                              max_length=10,                            # 최대길이 256 글자 혹은 byte 이하, 최대길이 150, 빈칸가능
                              choices=GENDER_CHOICES,                   # 선택옵션을 GENDER_CHOICES 튜플로한다
                              default='N')                              # 기본값을 N으로 설정

    #[보강요망] __str__ 문자열 화 함수 : 인스턴트 자체를 출력할 때의 형식을 지정해주는 함수 // 오지랖 책 보고 설명 보강
    def __str__(self):
        return self.nickname

    """
    
        @property :Decorators make defining new properties or modifying existing ones easy
        property 데코레이터는 존재하는 기능을 새로 정의하거나 수정할때 사용한다
        Profile 클래스에 이미 정의된 user, nickname, follow_set, picture, about, gender 밑에 새로운 함수를 추가 
        ?? 그럼 그냥 함수를 추가로 작성하는 것과 무슨차이?
        
    """

    @property
    def bookmark_count(self):
        return self.user_profiles.count()
        # count() 데이터의 개수를 샘


    @property                                                       # 나를 펄로우한 유저를 for 반복문으로 돌려서 전부 불러와서 담는다
    def get_follower(self):
        return [i.from_user for i in self.follower_user.all()]

    @property                                                       # 내가 펄로우한 유저를 for 반복문으로 돌려서 전체 리스트를 불러와서 배열을 담는다
    def get_following(self):
        return [i.to_user for i in self.follow_user.all()]

    @property                                                       # 나를 펄로우한 유저의 숫자를 확인함
    def follower_count(self):
        return len(self.get_follower)                               # len() 함수는 리스트에 들어있는 원소 개수, 그러니까 리스트의 크기를 알려준다

    @property                                                       # 내가 펄로우한 유저의 숫자를 확인함
    def following_count(self):
        return len(self.get_following)

    def is_follower(self, user):                                    # 나를 펄로워한 사람 한명을 표시
        return user in self.get_follower

    def is_following(self, user):                                   # 나를 표시
        return user in self.get_following
"""

    name: Relation
    기능: 회원들과의 관계를 보여주는 모델
    (models.Model) : 항상 Model 클래스를 상속받는다, pk 는 자동으로 생성
    
"""
class Relation(models.Model):
    from_user = models.ForeignKey(Profile,                          # 외래키를 Profile로 설정
                                  related_name='follow_user',       # Be careful with related_name에서 정의한 쿼리인 related_name 은 유일해야한다 나중에 검색하기 위한 태그
                                  on_delete=models.CASCADE)         # Profile이 삭제되면 함께 삭제됨
    to_user = models.ForeignKey(Profile,                            # 외래키를 Profile로 설정
                                related_name='follower_user',       # Be careful with related_name에서 정의한 쿼리인 related_name 은 유일해야한다 나중에 검색하기 위한 태그
                                on_delete=models.CASCADE)           # Profile이 삭제되면 함께 삭제됨
    created_at = models.DateTimeField(auto_now_add=True)            # auto_now_add : 시간을 새로 입력할때 사용, auto_now : 시간을 업데이트 할때 사용

    def __str__(self):                                              # __str__ 문자열 화 함수 : 인스턴트 자체를 출려할 때의 형식을 지정해주는 함수
        return "{} -> {}".format(self.from_user, self.to_user)      # 포매팅 : 결과 { self.from_user } -> { self.to_user }

    class Meta:
        unique_together = (
            ('from_user', 'to_user')
        )

"""

    [보강] - 소스: 오지랖
    모델에 메타 데이터를 추가
    https://docs.djangoproject.com/en/1.7/ref/models/options/
    unique_togeter: Sets of field names that, taken together, must be unique:
    -> A ManyToManyField cannot be included in unique_together 다대다 구조의 field는 unique_together를 사용할수 없다

"""