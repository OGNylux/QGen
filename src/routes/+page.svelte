<script lang="ts">
  import { WavyBackground } from "$lib/components/ui/WavyBackground/index";
  import NavBar from "$lib/components/navBar.svelte";
  import { ChevronDown } from "lucide-svelte";
</script>


<div class="scroll-smooth" id="top">
	<NavBar />
	<section class="h-screen relative">
	<WavyBackground className="max-w-4xl mx-auto pb-40">
		<p class="inter-var text-center text-2xl font-bold text-white md:text-4xl lg:text-7xl">
			QGen
		</p>
		<p class="inter-var mt-4 text-center text-base font-normal text-white md:text-lg">
			Minecraft Bedrock Quest Generator
		</p>
	</WavyBackground>
	<a href="/#functions" class="absolute bottom-20 flex justify-center w-full">
		<ChevronDown class="animate-bounce mb-5 cursor-pointer" />
	</a>
	</section>
</div>