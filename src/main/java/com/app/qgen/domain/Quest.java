package com.app.qgen.domain;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name = "quest")
public class Quest {
    @Id
    @GeneratedValue
    private Long id;
    private String questName;
    private String questDesc;

    public Quest(String questName, String questDesc) {
        this.questName = questName;
        this.questDesc = questDesc;
    }

    public Quest(Long id, String questName, String questDesc) {
        this.id = id;
        this.questName = questName;
        this.questDesc = questDesc;
    }

    public Quest() {
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getQuestName() {
        return questName;
    }

    public void setQuestName(String questName) {
        this.questName = questName;
    }

    public String getQuestDesc() {
        return questDesc;
    }

    public void setQuestDesc(String questDesc) {
        this.questDesc = questDesc;
    }
}
