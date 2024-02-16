<script lang="js">
    // @ts-ignore
    let rand;
    async function getRand() {
      const response = await fetch("http://localhost:80/rand")

      const random = await response.json();
      const test = random.number
      rand = test
      console.log(rand)
    }

    let foo = 0
	  let bar = 1
	  let result = null

    async function test2() {
      const res = await fetch('http://localhost:80/test', {
			method: 'POST',
			body: JSON.stringify({
				foo,
				bar
			  })
		  })
		
		  const json = await res.json()
		  result = JSON.stringify(json)
      
    }
  </script>
  <h1>Your number is {result}!</h1>
  <button on:click={() => test2()}>Get a random number</button>