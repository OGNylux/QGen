<script lang="ts">
  	import { WavyBackground } from "$lib/components/ui/WavyBackground/index";
  	import { ChevronDown, DollarSign, FastForward, Lollipop } from "lucide-svelte";
    import { Separator } from "bits-ui";
</script>

<div class="scroll-smooth">
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
		<ChevronDown class="animate-bounce mb-20 cursor-pointer" />
	</a>
	</section>
	<section class="sm:h-screen grid place-items-center" id="functions">
		<div
			class="w-full lg:w-4/5 xl:w-[70%] grid place-items-center md:place-items-start grid-cols-1 lg:grid-cols-3 relative"
		>
			<div
				class="h-full space-y-4 hover:bg-neutral-800 p-5 rounded-md cursor-pointer transition hover:-translate-y-1 mx-5"
			>
				<Lollipop class="w-14 h-14 text-emerald-700" />
				<h2 class="text-3xl font-bold">Easy</h2>
				<p class="text-neutral-400">
					Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
					At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
				</p>
			</div>
			<div class="absolute left-1/3 grid place-items-center top-0 h-full">
			<Separator.Root orientation="vertical" class="w-1 h-[90%] rounded-xl bg-emerald-600" />	
			</div>
			<div
				class="h-full space-y-4 hover:bg-neutral-800 p-5 rounded-md cursor-pointer transition hover:-translate-y-1 mx-5"
			>
				<FastForward class="w-14 h-14 text-emerald-700" />
				<h2 class="text-3xl font-bold">Fast</h2>
				<p class="text-neutral-400">
					Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
					At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
				</p>
			</div>
			<div class="absolute left-2/3 grid place-items-center top-0 h-full">
			<Separator.Root orientation="vertical" class="w-1 h-[90%] rounded-xl bg-emerald-600" />	
			</div>
			<div
				class="h-full space-y-4 hover:bg-neutral-800 p-5 rounded-md cursor-pointer transition hover:-translate-y-1 mx-5"
			>
				<DollarSign class="w-14 h-14 text-emerald-700" />
				<h2 class="text-3xl font-bold">Free</h2>
				<p class="text-neutral-400">
					Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
					At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
				</p>
			</div>
		</div>
	</section>
	
	<section class="grid mb-32 place-items-center mt-32 sm:mt-0" id="about">
		<div class="flex flex-col w-1/2 items-center bg-neutral-800 p-4 rounded-md text-center">
			<h3 class="text-3xl font-bold mb-3">About</h3>
			<p class="w-2/3">
				Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
				At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. 
				Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
				<br />
				At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. 
				Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. 
				Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.   
				Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum 
				zzril delenit augue duis dolore te feugait nulla facilisi. Lorem ipsum dolor sit amet,
			</p>
		</div>
	</section>
</div>