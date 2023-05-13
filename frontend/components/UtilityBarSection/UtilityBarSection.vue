<template>
  <div class="text-center text-app-gray-pearl">
    <div class="p-4">
      <Icon
        v-if="props.title === section.cvSentions"
        name="mingcute:document-line"
        class="text-5xl"
      />
      <div
        v-else-if="props.title === section.elements"
        class="text-2xl grid grid-cols-2"
      >
        <Icon name="mingcute:square-line" />
        <Icon name="mingcute:triangle-line" />
        <Icon name="mingcute:star-fill" />
        <Icon name="mingcute:round-line" />
      </div>
    </div>
    {{ capitalize(props.title) }}
  </div>
</template>

<script lang="ts" setup>
import { section } from "@/utils/templateTools/templateTools";
import { capitalize } from "@/utils/tools";

const props = defineProps<{ title: string }>();
</script>
