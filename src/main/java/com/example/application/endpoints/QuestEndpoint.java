package com.example.application.endpoints;

import com.example.application.Quest;
import com.example.application.QuestRepository;
import com.vaadin.flow.server.auth.AnonymousAllowed;
import dev.hilla.Endpoint;
import dev.hilla.Nonnull;

import java.util.List;

@Endpoint
@AnonymousAllowed
public class QuestEndpoint {
    private QuestRepository repository;

    QuestEndpoint(QuestRepository repository) {
        this.repository = repository;
    }

    public @Nonnull List<@Nonnull Quest> findAll() {
        return repository.findAll();
    }

    public Quest add(String questName, String questDesc) {
        return repository.save(new Quest(questName, questDesc));
    }

    public Quest update(Quest quest) {
        return repository.save(quest);
    }
}
