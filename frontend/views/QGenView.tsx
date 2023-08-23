import type Quest from 'Frontend/generated/com/example/application/Quest';
import { useEffect, useState } from 'react';
import { Button } from '@hilla/react-components/Button.js';
import { Checkbox } from '@hilla/react-components/Checkbox.js';
import { TextField } from '@hilla/react-components/TextField.js';
import { QuestEndpoint } from 'Frontend/generated/endpoints';

export default function QGenView() {
    const [questLine, setQuestLine] = useState(Array<Quest>());
    const [questName, setQuestName] = useState('');
    const [questDesc, setQuestDesc] = useState('');

    useEffect(() => {
        QuestEndpoint.findAll().then(setQuestLine)
    }, []);

    async function addQuest() {
        const saved = await QuestEndpoint.add(questName, questDesc);
        if(saved) {
            setQuestLine([...questLine, saved]);
            setQuestName('');
            setQuestDesc('');
        }
    }

    async function updateQuest(quest: Quest, questName: string, questDesc: string) {
        const saved = await QuestEndpoint.update( {
            ...quest, questName, questDesc
        });
        if(saved) {
            setQuestLine(questLine.map(existing => existing.id == saved.id ? saved : existing));
            setQuestName('');
            setQuestDesc('');
        }
    }

    return (
        <div className="p-m">
            <h1>Test</h1>
            <div className="flex-box gap-s">
                <TextField value={questName} onChange={e => setQuestName(e.target.value)}></TextField>
                <TextField value={questDesc} onChange={f => setQuestDesc(f.target.value)}></TextField>
                <Button theme="primary" onClick={addQuest}>Add</Button>
            </div>
            {questLine.map(quest => (
                <div key={quest.id}>
                    <span>{quest.questName} {quest.questDesc}</span>
                    <Button theme="primary"
                            onClick={() => updateQuest(quest, questName, questDesc)}>Add</Button>
                </div>
            ))}
        </div>
    );
}