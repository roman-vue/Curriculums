<template>
  <aside class="bg-zinc-800 h-screen p-4">
    <div class="flex flex-col-reverse divide-y divide-y-reverse">
      <div class="py-5"></div>
      <div class="overflow-x-scroll flex gap-3 py-5">
        <UtilityBarSection
          v-for="(tool, index) in TemplateTools.sections"
          :key="index"
          :title="tool"
        />
      </div>
    </div>
  </aside>
</template>

<script lang="ts" setup>
import UtilityBarSection from "@/components/UtilityBarSection/UtilityBarSection.vue";
import TemplateTools from "@/utils/templateTools/templateTools";
</script>
