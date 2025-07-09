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

### Vegetable Data Structure

```
images/no_bg/
├── basil_no_bg.png
├── cabbage_no_bg.png
├── kale_no_bg.png
├── onion_no_bg.png
├── raddish_no_bg.png
└── sweetpotato_no_bg.png
```

## Development

### Local Development
```bash
# Clone repository
git clone https://github.com/Amakran2003/sunoneorganic.git

# Navigate to project
cd sunoneorganic

# Serve locally (any HTTP server)
python -m http.server 8000
# or
npx serve .
```

### Testing Protocol

1. Cross-browser compatibility testing
2. Responsive design validation across viewport sizes
3. Touch interaction testing on mobile devices
4. Performance profiling for iframe loading
5. Accessibility compliance verification

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

## Performance Considerations

- Optimized image assets with background removal
- Lazy loading for viewport-based rendering
- Responsive image scaling
- Minimal CSS footprint
- CDN-delivered panorama content

## Browser Support Matrix

| Browser | Desktop | Mobile | Touch Support |
|---------|---------|--------|---------------|
| Chrome  | ✅      | ✅     | ✅            |
| Firefox | ✅      | ✅     | ✅            |
| Safari  | ✅      | ✅     | ✅            |
| Edge    | ✅      | ✅     | ✅            |

## Deployment

### GitHub Pages
Automated deployment via GitHub Actions workflow on push to main branch.

### Custom Hosting
Static files can be served from any HTTP server supporting:
- MIME type configuration for .avif images
- HTTPS (recommended for iframe embedding)
- Gzip compression for performance
