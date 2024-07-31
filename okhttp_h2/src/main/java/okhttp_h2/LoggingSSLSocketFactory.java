package okhttp_h2;

import javax.net.ssl.SSLSocketFactory;
import javax.net.ssl.SSLSocket;
import java.io.IOException;
import java.net.InetAddress;
import java.net.Socket;

public class LoggingSSLSocketFactory extends SSLSocketFactory {
    private SSLSocketFactory baseFactory;

    public LoggingSSLSocketFactory(SSLSocketFactory baseFactory) {
        this.baseFactory = baseFactory;
    }

    @Override
    public String[] getDefaultCipherSuites() {
        return baseFactory.getDefaultCipherSuites();
    }

    @Override
    public String[] getSupportedCipherSuites() {
        return baseFactory.getSupportedCipherSuites();
    }

    @Override
    public Socket createSocket(Socket s, String host, int port, boolean autoClose) throws IOException {
        Socket socket = baseFactory.createSocket(s, host, port, autoClose);
        logSSLSession(socket);
        return socket;
    }

    @Override
    public Socket createSocket(String host, int port) throws IOException {
        Socket socket = baseFactory.createSocket(host, port);
        logSSLSession(socket);
        return socket;
    }

    @Override
    public Socket createSocket(String host, int port, InetAddress localHost, int localPort) throws IOException {
        Socket socket = baseFactory.createSocket(host, port, localHost, localPort);
        logSSLSession(socket);
        return socket;
    }

    @Override
    public Socket createSocket(InetAddress host, int port) throws IOException {
        Socket socket = baseFactory.createSocket(host, port);
        logSSLSession(socket);
        return socket;
    }

    @Override
    public Socket createSocket(InetAddress address, int port, InetAddress localAddress, int localPort) throws IOException {
        Socket socket = baseFactory.createSocket(address, port, localAddress, localPort);
        logSSLSession(socket);
        return socket;
    }

    private void logSSLSession(Socket socket) {
        if (socket instanceof SSLSocket) {
            // 여기에 SSL/TLS 세션 정보를 로깅하는 코드를 추가합니다.
            System.out.println("SSL session started: " + ((SSLSocket) socket).getSession());
            // System.out.println("SSL session started.");
        }
    }
}