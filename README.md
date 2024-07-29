dynamically updated heatmap in an svg

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./result_dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./result_light.svg">
  <img alt="heatmap" src="./result_light.svg">
</picture>

### code

```md
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./result_dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./result_light.svg">
  <img alt="heatmap" src="./result_light.svg">
</picture>
```
