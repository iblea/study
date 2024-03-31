package com.iasdf.studyspring.domain;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Entity
public class Member {

    @Getter
    @Setter
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Getter
    @Setter
    // @Column(name = "username")
    // @Column(name = "name")
    private String name;


}
