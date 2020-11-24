# api-samples

- [EN](../README.md) | KO | [CN](README-CN.md)

[MCS 거래소](https://mycoinstory.com/) OPEN API 를 사용하기 위한 언어별 Sample 코드 입니다. Sample 을 제공하는 언어는 아래와 같습니다.

- [Python](../sample-python.py)
- Java (WIP)
- NodeJS (WIP)

각 언어별 Sample 은 최대한 간단하게 사용법을 파악할 수 있도록 라이브러리 의존성을 최소화하였고 코드의 중복을 허용하고 리팩토링을 하지 않았습니다. 사용법을 파악하는 용도로 활용하시는 것을 추천드립니다.

위 리스트에 OPEN API 를 활용하기 위해 필요한 언어가 없다면 [이슈 페이지](https://github.com/mcs-exchange/api-samples/issues)에 요청해주시면 추가하도록 하겠습니다.

## 요구사항
Sample 을 사용하기 위해서 MCS 거래소에 API_KEY 와 API_SECRET 이 필요합니다. MCS 에 로그인 한 후 [API 발급 페이지](https://mycoinstory.com/account/api) 에서 API 키를 발급해야 합니다.
각 언어별 Sample 은 아래 버전에서 정상 동작을 확인하였습니다.

|Language | Version       |
|---------|:-------------:|
|Python   | >= `3.6.x`    |
|Java     | >= `1.8.x`    |
|NodeJS   | >= `v14.15.1` |

## 실행
코드에 `<INPUT_YOUR_API_KEY>` `<INPUT_YOUR_API_SECRET>` 로 된 부분을 위에서 발급받은 본인의 키로 변경한 후 각 언어별 실행 명령어를 입력합니다.

### Python
```python 
python sample-python.py
```
### JAVA
```java
```
### NodeJS
```nodejs
```

## 피드백
코드나 문서에 문제가 있다면 [이슈 페이지](https://github.com/mcs-exchange/api-samples/issues) 에 이슈를 남겨주시길 바랍니다. 최대한 빠르게 피드백 하겠습니다.
