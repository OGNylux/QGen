package com.app.qgen.controller;

import com.app.qgen.domain.Quest;
import com.app.qgen.repository.QuestRepository;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.net.URI;
import java.net.URISyntaxException;
import java.util.List;

@RestController
@RequestMapping("/quests")
public class QuestsController {

    private final QuestRepository questRepository;

    public QuestsController(QuestRepository questRepository) {
        this.questRepository = questRepository;
    }

    @GetMapping
    public List<Quest> getQuests() {
        return questRepository.findAll();
    }

    @GetMapping("/{id}")
    public Quest getQuest(@PathVariable Long id) {
        return questRepository.findById(id).orElseThrow(RuntimeException::new);
    }

    @PostMapping
    public ResponseEntity createClient(@RequestBody Quest quest) throws URISyntaxException {
        Quest savedQuest = questRepository.save(quest);
        return ResponseEntity.created(new URI("/quests/" + savedQuest.getId())).body(savedQuest);
    }

    @PutMapping("/{id}")
    public ResponseEntity updateClient(@PathVariable Long id, @RequestBody Quest quest) {
        Quest currentQuest = questRepository.findById(id).orElseThrow(RuntimeException::new);
        currentQuest.setQuestName(quest.getQuestName());
        currentQuest.setQuestDesc(quest.getQuestDesc());
        currentQuest = questRepository.save(quest);

        return ResponseEntity.ok(currentQuest);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity deleteQuest(@PathVariable Long id) {
        questRepository.deleteById(id);
        return ResponseEntity.ok().build();
    }
}
