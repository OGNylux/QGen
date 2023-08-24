package com.app.qgen;

import com.app.qgen.domain.Quest;
import com.app.qgen.repository.QuestRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

@Component
public class BootstrapInitialData implements CommandLineRunner {

    private final QuestRepository questRepository;

    public BootstrapInitialData(QuestRepository questRepository) {
        this.questRepository = questRepository;
    }

    @Override
    public void run(String... args) {
        for (int i = 0; i < 10; i++) {
            questRepository.save(new Quest("t", "x"));
        }
    }
}
