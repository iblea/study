package com.iasdf.studyspring;

import javax.sql.DataSource;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.jdbc.core.JdbcTemplate;

import com.iasdf.studyspring.repository.MemberRepository;
import com.iasdf.studyspring.repository.MemoryMemberRepository;
import com.iasdf.studyspring.aop.TimeTraceAop;
import com.iasdf.studyspring.repository.JdbcMemberRepository;
import com.iasdf.studyspring.repository.JdbcTemplateMemberRepository;
import com.iasdf.studyspring.repository.JpaMemberRepository;
import com.iasdf.studyspring.repository.SpringDataJpaMemberRepository;
import com.iasdf.studyspring.service.MemberService;

import jakarta.persistence.EntityManager;

@Configuration
public class SpringConfig {

    // private DataSource dataSource;
    // final EntityManager em;
    private final MemberRepository memberRepository;

    // @Autowired
    // public SpringConfig(DataSource dataSource) {
    //     this.dataSource = dataSource;
    // }

    // @Autowired
    // public SpringConfig(EntityManager em) {
    //     this.em = em;
    // }

    @Autowired
    public SpringConfig(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }

    @Bean
    public MemberService memberService() {
        // return new MemberService(memberRepository());
        return new MemberService(memberRepository);
    }

    // @Bean
    // public MemberRepository memberRepository() {
    //     // return new MemoryMemberRepository();
    //     // return new JdbcMemberRepository(dataSource);
    //     // return new JdbcTemplateMemberRepository(dataSource);
    //     return new JpaMemberRepository(em);
    // }

    @Bean
    public TimeTraceAop timeTraceAop() {
        return new TimeTraceAop();
    }

}
