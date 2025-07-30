# Sun One Organic - 360° Vegetable Yield Application

A web application implementing 360° panoramic visualization of vegetable yields using embedded Momento360 viewer technology.

## Technical Features

- **360° Panorama Integration**: Momento360 iframe embedding with custom parameters
- **Responsive CSS Grid**: Flexible layout system with mobile-first approach
- **Modern CSS3**: Flexbox, CSS Grid, custom properties, and media queries
- **Component-Based Layout**: Modular HTML structure with semantic elements
- **Progressive Enhancement**: Graceful degradation for legacy browsers

## Architecture

### Frontend Stack
- HTML5 semantic markup
- CSS3 with modern layout techniques
- Embedded iframe integration
- No JavaScript dependencies (pure CSS implementation)


## Development

## Integration

### Momento360 API Parameters
```javascript
{
  heading: 344.07,        // Initial viewing direction (degrees)
  pitch: -47.98,          // Vertical angle (degrees)
  'field-of-view': 81,    // Zoom level (degrees)
  size: 'medium',         // Player dimensions
  'display-plan': true    // Show navigation controls
}
```

### Wix CMS Integration
```html
<iframe 
    src="https://momento360.com/e/u/47b0c03467b94acb913801f5e6cfb734?utm_campaign=embed&utm_source=other&heading=344.07&pitch=-47.98&field-of-view=81&size=medium&display-plan=true"
    width="100%" 
    height="500px" 
    frameborder="0" 
    allowfullscreen>
</iframe>
```


