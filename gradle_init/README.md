
## Package Name 변경

package name : `okhttp_h2`
  - `okhttp_h2` 내용을 `grep` 으로 검색해서 모두 변경할 것.
  - `build.gradle.kts` 의 `mainClass.set("okhttp_h2.MainKt")` 변경
  - `src/main/java/okhttp_h2/` 디렉토리 이름 변경

아래 명령어로 `.kts`, `.java` 파일에서 `okhttp_h2` 를 모두 찾을 수 있다.

```sh
find . -regex ".*\.\(kts\|java\)$" -type f -exec grep -Hn --color "okhttp_h2" {} \;
```

## App Name 변경

App_Name : `okhttp2`
  - `settings.gradle.kts` - `rootProject.name = "okhttp2"` 변경




구조는 아래와 같다.

- `src/` - 소스 디렉토리
  - `main/`
    - `java/` - 자바 실제 소스
      - `<pkg_name>/`
    - `resources/` - 리소스
  - `test/`
    - `java/` - 테스트 소스
      - `<pkg_name>/`
    - `resources/` - 테스트 리소스
- `build.gradle.kts` - gradle 빌드 파일
- `settings.gradle.kts` - gradle 설정 파일
- `gradlew` - gradle 스크립트
- `gradlew.bat`
- `gradle/`
  - `wrapper/`
    - `gradle-wrapper.jar`
    - `gradle-wrapper.properties`


빌드
```sh
./gradlew build
```

디펜던시 초기화 / 업데이트
```sh
./gradlew build --refresh-dependencies
```

빌드결과물 (`.jar`) 실행
```java
java -jar build/libs/<App Name>.jar
```

