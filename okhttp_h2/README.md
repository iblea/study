

# 빌드 방법

### 요구사항
- Java 17 설치
- Gradle 설치
- `extract-tls-secrets-4.0.0.jar` 필요 (프로젝트 파일에 존재)
  - `sslkeylog.log` 를 생성하기 위한 모듈

```bash
./gradlew build
```


# 실행

```bash
start.sh
```

실행 시 `start.sh` 스크립트가 위치한 경로에 `sslkeylog.log` 파일이 생성된다. \
해당 파일을 통해 `OkHttp3`가 통신한 TLS 패킷을 Wireshark로 확인할 수 있다.

