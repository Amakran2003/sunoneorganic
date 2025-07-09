# Sun One Organic - 360° Vegetable Yield Test Page

This test page showcases your 360° panorama photo of vegetable yields in a beautiful, modern layout.

## Features

- **360° Panorama Integration**: Embedded Momento360 viewer
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Modern UI**: Beautiful gradient background with glassmorphism effects
- **Vegetable Showcase**: Grid layout featuring your main vegetables
- **Interactive Elements**: Hover effects and smooth animations

## Vegetables Featured

- 🌿 Basil
- 🧄 Garlic  
- 🥬 Cabbage
- 🧅 Onion
- 🍠 Sweet Potatoes
- 🥬 Kale
- 🌶️ Radish
- And more...

## Testing the Page

1. Open `index.html` in any web browser
2. The 360° panorama should load automatically
3. Test navigation: click and drag to look around
4. Test zoom: use mouse wheel or pinch gestures on mobile
5. Verify responsive design on different screen sizes

## For Wix Implementation

To add this to your Wix website:

1. **Add HTML Embed Component**:
   - In Wix Editor, add an "HTML iframe" or "Custom Code" element
   - Paste the iframe code:
   ```html
   <iframe 
       src="https://momento360.com/e/u/47b0c03467b94acb913801f5e6cfb734?utm_campaign=embed&utm_source=other&heading=344.07&pitch=-47.98&field-of-view=81&size=medium&display-plan=true"
       width="100%" 
       height="500px" 
       frameborder="0" 
       allowfullscreen>
   </iframe>
   ```

2. **Styling in Wix**:
   - Set the iframe dimensions (recommended: 100% width, 400-600px height)
   - Add border radius for rounded corners if desired
   - Consider adding a container with background color/shadow

3. **Mobile Optimization**:
   - Test on mobile preview in Wix
   - Adjust height for mobile if needed (300-400px recommended)

## Customization Options

You can modify the Momento360 URL parameters:
- `heading`: Initial viewing direction (0-360 degrees)
- `pitch`: Initial vertical angle (-90 to 90 degrees)
- `field-of-view`: Zoom level (30-120 degrees)
- `size`: Player size (small, medium, large)

## Notes

- The panorama loads from Momento360's servers
- Ensure stable internet connection for best performance
- The embed is mobile-friendly and touch-enabled
- Consider adding loading indicators for slower connections

## Browser Compatibility

- Chrome, Firefox, Safari, Edge (latest versions)
- iOS Safari, Chrome Mobile
- Supports both desktop and mobile interactions
