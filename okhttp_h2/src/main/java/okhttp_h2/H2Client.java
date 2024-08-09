package okhttp_h2;

import java.util.Collections;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;

import javax.net.ssl.*;
import java.util.Arrays;

import java.io.File;
import java.io.IOException;
import java.io.OutputStream;
import java.security.KeyStore;

import okhttp3.ConnectionPool;
import okhttp3.MediaType;
import okhttp3.MultipartBody;
import okhttp3.OkHttpClient;
import okhttp3.Protocol;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;


public class H2Client {

    private static OkHttpClient okHttpClient = null;
    private static List<Protocol> protocols = null;


    public static void create()
    {
        if (protocols == null) {
            setProtocols();
        }
        if (okHttpClient == null) {
            okHttpClient = createHttpClient(10, 30000);   // 10개의 연결, 30초 유지
        }
    }

    public static OkHttpClient getClient() {
        return okHttpClient;
    }

    public static List<Protocol> getProtocols() {
        return protocols;
    }

    public H2Client()
    {
        H2Client.create();
    }

    public H2Client(String sslkeylogPath)
    {
        H2Client.create();
    }



    // private SSLSocketFactory getSslSocketFactory()
    //     throws Exception
    // {
    //     SSLContext sslContext = SSLContext.getInstance("TLS");
    //     // 기본 키 스토어 및 트러스트 스토어 설정 (필요에 따라 커스터마이즈 가능)
    //     KeyManagerFactory keyManagerFactory = KeyManagerFactory.getInstance(KeyManagerFactory.getDefaultAlgorithm());
    //     TrustManagerFactory trustManagerFactory = TrustManagerFactory.getInstance(TrustManagerFactory.getDefaultAlgorithm());
    //     keyManagerFactory.init(null, null); // null은 기본 키 스토어 사용
    //     trustManagerFactory.init((KeyStore) null); // null은 기본 트러스트 스토어 사용

    //     // SSLContext 초기화
    //     sslContext.init(keyManagerFactory.getKeyManagers(), trustManagerFactory.getTrustManagers(), null);

    //     // 커스터마이즈된 SSLSocketFactory 생성
    //     SSLSocketFactory sslSocketFactory = sslContext.getSocketFactory();
    //     // SSL/TLS 키 로그를 출력하는 커스텀 SSLSocketFactory 반환
    //     return new LoggingSSLSocketFactory(sslSocketFactory);
    // }

    // private X509TrustManager getDefaultTrustManager() throws Exception {
    //     TrustManagerFactory trustManagerFactory = TrustManagerFactory.getInstance(TrustManagerFactory.getDefaultAlgorithm());
    //     trustManagerFactory.init((KeyStore) null); // null은 기본 트러스트 스토어 사용
    //     TrustManager[] trustManagers = trustManagerFactory.getTrustManagers();
    //     if (trustManagers.length != 1 || !(trustManagers[0] instanceof X509TrustManager)) {
    //         throw new IllegalStateException("Unexpected default trust managers:" + Arrays.toString(trustManagers));
    //     }
    //     return (X509TrustManager) trustManagers[0];
    // }

    private static void setProtocols() {
        if (protocols != null) {
            protocols = null;
        }
        protocols = new ArrayList<>();
        // protocols.add(Protocol.H2_PRIOR_KNOWLEDGE);
        protocols.add(Protocol.HTTP_2);
        protocols.add(Protocol.HTTP_1_1);
    }


    private static OkHttpClient createHttpClient(int maxTotalConnections, long connectionKeepAliveTimeInMillis)
    {
        ConnectionPool connectionPool = new ConnectionPool(
            maxTotalConnections,
            connectionKeepAliveTimeInMillis,
            TimeUnit.MILLISECONDS
        );

        // SSLSocketFactory sslSocketFactory = getSslSocketFactory();
        // X509TrustManager trustManager = getDefaultTrustManager();

        return new OkHttpClient.Builder()
            .followRedirects(true)
            .protocols(protocols)
            .retryOnConnectionFailure(true)
            .connectionPool(connectionPool)
            // .sslSocketFactory(sslSocketFactory, trustManager)
            .build();
    }

    public void showResponse(Request request)
        throws IOException
    {
        OkHttpClient okClient = H2Client.getClient();
        Response response = okClient.newCall(request).execute();
        if (response.code() < 200 || response.code() >= 300) {
            System.out.println("Request Code is not 2xx: " + response.code());
            return ;
        }

        String responsePage = response.body().string();
        System.out.println("======================================================");
        System.out.println(responsePage);
        System.out.println("======================================================");
    }

    public void requestGet(String url)
        throws IOException
    {
        System.out.println("URL: " + url);
        Request request = new Request.Builder()
            .url(url)
            .build();
        showResponse(request);
    }

    public void uploadFile(String url, String filePath) throws IOException {
        System.out.println("URL: " + url);
        File file = new File(filePath);
        System.out.println("File Path: " + file.getAbsolutePath());
        System.out.println("File Name: " + file.getName());

        // 파일을 위한 RequestBody 생성
        // RequestBody fileBody = RequestBody.create(MediaType.parse("application/octet-stream"), file);
        // RequestBody fileBody = RequestBody.Companion.create(file, MediaType.parse("application/octet-stream"));
        RequestBody fileBody = RequestBody.Companion.create(file, MediaType.parse("multipart/form-data"));

        // MultipartBody를 사용하여 파일과 다른 폼 데이터 포함
        RequestBody requestBody = new MultipartBody.Builder()
                .setType(MultipartBody.FORM)
                .addFormDataPart("upfiled1", file.getName(), fileBody)
                // 추가적인 폼 데이터가 필요한 경우 아래와 같이 추가
                // .addFormDataPart("upfiled2", file2.getName(), file2body)
                .build();

        // Request 객체 생성
        Request request = new Request.Builder()
                .url(url)
                .post(requestBody)
                .build();

        showResponse(request);
    }

}
