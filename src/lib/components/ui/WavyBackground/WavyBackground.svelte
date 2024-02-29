<script lang="ts">
    import { cn } from "$lib/utils/cn";
    import { createNoise3D } from "simplex-noise";
    import { onMount } from "svelte";
    
    export let className = void 0;
    export let containerClassName = void 0;
    export let colors = void 0;
    export let waveWidth = void 0;
    export let blur = 10;
    export let speed = "fast";
    
    const noise = createNoise3D();
    let w, h, i, x: number;
    let nt: number = 0;
    let canvas: any;
    let ctx: CanvasRenderingContext2D;
    let canvasRef: any;
    let animationId: number;

                             //emerald 600  emerald 500  teal 600   teal 500  cyan 500
    const waveColors = colors ?? ["#059669", "#10b981", "#0d9488", "#14b8a6", "#06b6d4"];

    const getSpeed = () => {
      switch (speed) {
        case "slow":
          return 1e-3;
        case "fast":
          return 4e-3;
        default:
          return 1e-3;
      }
    };

    const init = () => {
      canvas = canvasRef;
      ctx = canvas.getContext("2d");
      ctx.canvas.width = window.innerWidth;
      ctx.canvas.height = window.innerHeight;
      
      w = ctx.canvas.width;
      h = ctx.canvas.height;
      ctx.filter = `blur(${blur}px)`;
      nt = 0;

      window.onresize = function() {
        w = ctx.canvas.width = window.innerWidth;
        h = ctx.canvas.height = window.innerHeight;
        ctx.filter = `blur(${blur}px)`;
      };

      render();
    };     

    const drawWave = (n: number) => {
      nt += getSpeed();

      for (i = 0; i < n; i++) {
        ctx.beginPath();
        ctx.lineWidth = waveWidth || 50;
        ctx.strokeStyle = waveColors[i % waveColors.length];

        for (x = 0; x < w; x += 5) {
          var y = noise(x / 800, 0.3 * i, nt) * 100;
          ctx.lineTo(x, y + h * 0.5);
        }

        ctx.stroke();
        ctx.closePath();
      }
    };
  
    const render = () => {
      ctx.fillStyle = "#171717";
      //ctx.globalAlpha = waveOpacity || 0.5;
      ctx.fillRect(0, 0, w, h);
      drawWave(5);
    };

    onMount(() => {
      init();

		  window.addEventListener('resize', resize);
    });

    const resize = () => {
      cancelAnimationFrame(animationId);
      animationId = requestAnimationFrame(render);
      console.log("resize");
    };

    </script>
    
<div class={cn('flex h-screen flex-col items-center justify-center', containerClassName)} on:resize={() => resize()}>
  <canvas class="absolute inset-0 z-0" bind:this={canvasRef} id="canvas" />
  <div class={cn('relative z-10', className)} {...$$props}>
    <slot />
  </div>
</div>