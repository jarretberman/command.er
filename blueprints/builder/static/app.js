class DeckBuilder {
    /** handles all deck building requirements */

    constructor(){
        this.name = null
        this.commander = null
        this.deck = new Set()
        this.commanders()
    }


    //asynchronous function to query scryfall api
    async commanders() {
        const response = await axios.get('https://api.scryfall.com/cards/search?order=cmc&q=legal%3Acommander%20is%3Acommander')
        this.commanderChoices = JSON.parse(response.data.data)

        console.log(response)
    }

    async commanderCards(commander) {
        
        const colors = commander.color_identity.join('')
        const response = await axios.get(`https://api.scryfall.com/cards/search?order=cmc&q=commander%3A${colors}%20legal%3Acommander`)
        
        this.cardChoices = JSON.parse(response.data.data)
    }

    pushToDeck(card) {
        if(!this.deck.has(card.id)){
            this.deck.add(card.id)
            return true
        }

        return false
    }

    
}