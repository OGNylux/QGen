def createMainJS():
    script = """import * as quest from "./quest.js"

quest.main()"""
    return script


def createQuestJS():
    script = """import { world, system } from "@minecraft/server"
import * as hud from "./questHud.js"
import * as checkItems from "./questCompletion.js"


export function main() {
    interactedWithNPC()
    hud.main()
    checkItems.main()
}

export const newLine = Array(8).fill("\\n")
const validNPCs = ["pb:hugotest", "pb:hugo"]

function interactedWithNPC() {
    world.beforeEvents.playerInteractWithEntity.subscribe((event) => {
        const {player, target} = event
        if(validNPCs.includes(target.typeId)) {
            openDialogue(player, target)
        }
    })
}

export function openDialogue(player, npc, state = getState(npc), index = "00") {
    npc.getTags().forEach(tag => {
        if (tag.includes("QGenQuest")) {
            system.run(() => {
                npc.runCommand(`dialogue open @s ${player.name} ${tag}.${state}${index}`)
            })
        } 
    })
}

function getState(target) {
    return target.hasTag("notFinished") ? "notFinished" : target.hasTag("finished") ? "finished" : "intro";
}
"""
    return script


def createQuestCompletionJS():
    script = """import { world, system, ItemStack } from "@minecraft/server"
import { QGenQuestConditions } from "./questData.js"
import { openDialogue } from "./quest.js"

let sceneCounter = 0

export function main() {
    checkItems()
}

function checkItems() {
    system.afterEvents.scriptEventReceive.subscribe((event) => {
        const {id, sourceEntity, initiator} = event
        if(id === "pb:checkConditions") {
            sourceEntity.getTags().forEach(tag => {
                if (tag.includes("QGenQuest")) {
                    checkLookupTable(tag, initiator, sourceEntity)
                } 
            })
        }
    })
}

function checkLookupTable(tag, player, npc) {
    QGenQuestConditions.forEach(quest => {
        if(tag == quest.name && checkAllConditions(player, npc, quest)) {
            giveRewards(player, quest)
            removeQuestItem(player, quest)
            npc.removeTag("notFinished")
            npc.addTag("finished")
            openDialogue(player, npc, "finished")
        }
    });
}

function giveRewards(player, quest) {
    quest.rewards.forEach(reward => {
        if(reward.items) reward.items.forEach(item => addQuestItem(item, player))
        if(reward.tags) reward.tags.forEach(tag => addQuestTag(tag))
    })
}

function addQuestItem(item, player) {
    const inventory = player.getComponent("minecraft:inventory").container;
    const itemStack = new ItemStack(item.id, item.amount)
    inventory.addItem(itemStack);
}

function addQuestTag(tag) {
    for (const player of world.getPlayers()) {
        if(player.hasTag("host")) player.addTag(tag)
    }
}

function removeQuestItem(player, quest) {
    quest.conditions.forEach(condition => {
        if(condition.items) condition.items.forEach(item => player.runCommand(`clear @s ${item.id} ${item.data} ${item.amount}`))
    })

}

function checkItemConditions(player, items) {
    return !items || items.every(item => checkItemAmount(player, item.id) >= item.amount);
}

function checkTagConditions(player, tags) {
    return !tags || tags.every(tag => player.getTags().includes(tag));
}

function checkAllConditions(player, npc, quest) {
    const condition = quest.conditions.every(condition =>
        checkItemConditions(player, condition.items) && checkTagConditions(player, condition.tags)
    );
    if(!condition) openDialogue(player, npc, "notFinished", getNewSceneIndex(quest))
    return condition;
}

function getNewSceneIndex(quest) {
    sceneCounter = (sceneCounter < quest.notFinishedTexts-1 ? sceneCounter+1 : 0)
    return sceneCounter.toString().padStart(2, "0")
}

function checkItemAmount(player, itemId) {
    const inventory = player.getComponent("minecraft:inventory").container;
    let itemAmount = 0;
    for (let slot = 0; slot < inventory.size; slot++) {
        let item = inventory.getItem(slot);
        if (item?.typeId != itemId) continue;
        itemAmount += item.amount;
    }
    return itemAmount;
}"""
    return script


def createQuestHudJS():
    script = """import { world, system } from "@minecraft/server"
import { newLine } from "./quest.js"

export function main() {
    questHUD()
    showHUDAtJoin()
}

function showHUDAtJoin() {
    world.afterEvents.playerSpawn.subscribe((event) => {
        const { player } = event
        player.getTags().forEach(tag => {
            if (tag.includes("QGenQuest")) {
                player.onScreenDisplay.setTitle(["updateQuest", { translate: `qgen.title.${tag}` }], {fadeInDuration: 20, stayDuration: 9999999, fadeOutDuration: 0, subtitle: { translate: `qgen.subtitle.${tag}`, with: newLine } })
            } 
        })
    })
}

function questHUD() {
    system.afterEvents.scriptEventReceive.subscribe((event) => {
        const {id} = event
        if(id === "pb:showHUD" || id === "pb:hideHUD") {
            for (const player of world.getPlayers()) {
                player.getTags().forEach(tag => {
                    if (tag.includes("QGenQuest")) {
                        toggleHUD(tag, id)
                    } 
                })
            }
        }
    })
}

function toggleHUD(currentQuest, id) {
    for (const player of world.getPlayers()) {
        if(id === "pb:showHUD") player.onScreenDisplay.setTitle(["updateQuest", { translate: `qgen.title.${currentQuest}` }], {fadeInDuration: 20, stayDuration: 9999999, fadeOutDuration: 0, subtitle: { translate: `qgen.subtitle.${currentQuest}`, with: newLine } })
        if(id === "pb:hideHUD") {
            player.onScreenDisplay.setTitle(["updateQuest", { translate: `qgen.title.${currentQuest}` }], {fadeInDuration: 0, stayDuration: 1, fadeOutDuration: 20, subtitle: { translate: `qgen.subtitle.${currentQuest}`, with: newLine } })
            player.removeTag(currentQuest)
        }
    }
}"""
    return script
