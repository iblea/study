package com.iasdf.studyspring;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import com.iasdf.studyspring.repository.MemberRepository;
import com.iasdf.studyspring.repository.MemoryMemberRepository;
import com.iasdf.studyspring.service.MemberService;

@Configuration
public class SpringConfig {

    @Bean
    public MemberService memberService() {
        return new MemberService(memberRepository());
    }

    @Bean
    public MemberRepository memberRepository() {
        return new MemoryMemberRepository();
    }
}