<script>
    import { flyAndScale } from "$lib/utils/transitions";
    import { Menubar } from "bits-ui";
</script>

<nav class="z-20 backdrop-blur pt-5 sticky grid place-items-center top-0 left-0 w-full select-none">
	<div class="bg-neutral-800 flex justify-between p-3 rounded-md w-full lg:w-4/5 xl:w-[70%]">
		<Menubar.Root class="w-full flex items-center justify-center">
			<Menubar.Menu>
			  <Menubar.Trigger
				class="inline-flex w-20 items-center justify-center rounded-md px-3 py-1 data-[highlighted]:bg-neutral-700 data-[state=open]:bg-neutral-700 hover:bg-neutral-700"
				>Home</Menubar.Trigger
			  >
			  <Menubar.Content
				class="z-50 w-32 max-w-[220px] rounded-xl bg-neutral-900 border-2 border-neutral-800 py-1.5 px-3 shadow-popover !ring-0 !ring-transparent "
				transition={flyAndScale}
				align="center"
				sideOffset={3}
			  >
				<div class="flex flex-col">
					<a class="hover:bg-neutral-800 rounded-md px-2" href="/#top">Home</a>
				  	<a class="hover:bg-neutral-800 rounded-md px-2" href="/#functions">QGen</a>
				  	<a class="hover:bg-neutral-800 rounded-md px-2" href="/#about">About</a>
				</div>
			  </Menubar.Content>
			</Menubar.Menu>
			<a class="inline-flex w-20 items-center justify-center rounded-md px-3 py-1 hover:bg-neutral-700" href="/docs">Docs</a>
			<div class="flex grow justify-center">
				<img src="logo.svg" alt="" class="w-28">
			</div>
			<div class="w-20">
			</div>
			<a class="inline-flex w-20 items-center justify-center rounded-md px-3 py-1 hover:bg-neutral-700" href="/editor">Editor</a>
		</Menubar.Root>
	</div>
</nav>