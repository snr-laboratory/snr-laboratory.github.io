#!/usr/bin/env python
# -*- coding: utf-8 -*-

url_base = "https://www.snr-lab.org/inventory/index.html?label="

# in svg, 1 unit is 1/96 inch

svg_base = """<svg xmlns="http://www.w3.org/2000/svg"
     xmlns:xlink="http://www.w3.org/1999/xlink"
     width="11in" height="8.5in">
  <defs>
    <symbol id="logo">

<g id="gnuplot_canvas">
<rect x="0" y="0" width="640" height="480" fill="none"/>
<defs>
	<circle id='gpDot' r='0.5' stroke-width='0.5' stroke='currentColor'/>
	<path id='gpPt0' stroke-width='0.222' stroke='currentColor' d='M-1,0 h2 M0,-1 v2'/>
	<path id='gpPt1' stroke-width='0.222' stroke='currentColor' d='M-1,-1 L1,1 M1,-1 L-1,1'/>
	<path id='gpPt2' stroke-width='0.222' stroke='currentColor' d='M-1,0 L1,0 M0,-1 L0,1 M-1,-1 L1,1 M-1,1 L1,-1'/>
	<rect id='gpPt3' stroke-width='0.222' stroke='currentColor' x='-1' y='-1' width='2' height='2'/>
	<rect id='gpPt4' stroke-width='0.222' stroke='currentColor' fill='currentColor' x='-1' y='-1' width='2' height='2'/>
	<circle id='gpPt5' stroke-width='0.222' stroke='currentColor' cx='0' cy='0' r='1'/>
	<use xlink:href='#gpPt5' id='gpPt6' fill='currentColor' stroke='none'/>
	<path id='gpPt7' stroke-width='0.222' stroke='currentColor' d='M0,-1.33 L-1.33,0.67 L1.33,0.67 z'/>
	<use xlink:href='#gpPt7' id='gpPt8' fill='currentColor' stroke='none'/>
	<use xlink:href='#gpPt7' id='gpPt9' stroke='currentColor' transform='rotate(180)'/>
	<use xlink:href='#gpPt9' id='gpPt10' fill='currentColor' stroke='none'/>
	<use xlink:href='#gpPt3' id='gpPt11' stroke='currentColor' transform='rotate(45)'/>
	<use xlink:href='#gpPt11' id='gpPt12' fill='currentColor' stroke='none'/>
	<path id='gpPt13' stroke-width='0.222' stroke='currentColor' d='M0,1.330 L1.265,0.411 L0.782,-1.067 L-0.782,-1.076 L-1.265,0.411 z'/>
	<use xlink:href='#gpPt13' id='gpPt14' fill='currentColor' stroke='none'/>
	<filter id='textbox' filterUnits='objectBoundingBox' x='0' y='0' height='1' width='1'>
	  <feFlood flood-color='white' flood-opacity='1' result='bgnd'/>
	  <feComposite in='SourceGraphic' in2='bgnd' operator='atop'/>
	</filter>
	<filter id='greybox' filterUnits='objectBoundingBox' x='0' y='0' height='1' width='1'>
	  <feFlood flood-color='lightgrey' flood-opacity='1' result='grey'/>
	  <feComposite in='SourceGraphic' in2='grey' operator='atop'/>
	</filter>
</defs>
<g fill="none" color="white" stroke="currentColor" stroke-width="2.00" stroke-linecap="butt" stroke-linejoin="miter">
</g>
<g fill="none" color="black" stroke="currentColor" stroke-width="2.00" stroke-linecap="butt" stroke-linejoin="miter">
</g>
<g fill="none" color="black" stroke="currentColor" stroke-width="2.00" stroke-linecap="butt" stroke-linejoin="miter">
</g>
	<g id="gnuplot_plot_1" ><title>f(x)</title>
<g fill="none" color="white" stroke="black" stroke-width="20.00" stroke-linecap="butt" stroke-linejoin="miter">
</g>
<g fill="none" color="black" stroke="currentColor" stroke-width="20.00" stroke-linecap="butt" stroke-linejoin="miter">
	<path stroke='rgb(255,   0,   0)'  d='M44.96,416.95 L50.96,391.87 L56.96,374.12 L62.96,362.20 L68.96,355.36 L74.96,353.32 L80.95,356.17 L86.95,364.39
		L92.95,379.04 L98.95,402.23 L104.95,438.45 M134.94,418.21 L140.94,373.84 L146.94,342.44 L152.94,319.52 L158.94,302.94
		L164.93,291.63 L170.93,285.09 L176.93,283.19 L182.93,286.21 L188.93,294.87 L194.93,310.63 L200.92,336.51 L206.92,379.46
		L212.92,462.05 M224.92,445.86 L230.92,346.97 L236.92,287.47 L242.91,244.67 L248.91,211.43 L254.91,184.58 L260.91,162.42
		L266.91,143.93 L272.91,128.45 L278.90,115.55 L284.90,104.91 L290.90,96.31 L296.90,89.60 L302.90,84.65 L308.90,81.39
		L314.90,79.78 L320.89,79.78 L326.89,81.39 L332.89,84.65 L338.89,89.60 L344.89,96.31 L350.89,104.91 L356.89,115.55
		L362.88,128.45 L368.88,143.93 L374.88,162.42 L380.88,184.58 L386.88,211.43 L392.88,244.67 L398.87,287.47 L404.87,346.97
		L410.87,445.86 M422.87,462.05 L428.87,379.46 L434.87,336.51 L440.86,310.63 L446.86,294.87 L452.86,286.21 L458.86,283.19
		L464.86,285.09 L470.86,291.63 L476.85,302.94 L482.85,319.52 L488.85,342.44 L494.85,373.84 L500.85,418.21 M530.84,438.45
		L536.84,402.23 L542.84,379.04 L548.84,364.39 L554.84,356.17 L560.83,353.32 L566.83,355.36 L572.83,362.20 L578.83,374.12
		L584.83,391.87 L590.83,416.95  '/></g>
	</g>
	<g id="gnuplot_plot_2" ><title>log10(1.0+rand(0)/5.0)-clip(x)</title>
<g fill="none" color="white" stroke="rgb(255,   0,   0)" stroke-width="10.00" stroke-linecap="butt" stroke-linejoin="miter">
</g>
<g fill="none" color="black" stroke="currentColor" stroke-width="10.00" stroke-linecap="butt" stroke-linejoin="miter">
	<path stroke='rgb(  0, 128, 255)'  d='M20.97,99.79 L26.97,92.03 L32.97,85.96 L38.97,92.50 L44.96,79.03 L50.96,81.30 L56.96,79.47 L62.96,80.54
		L68.96,72.99 L74.96,76.03 L80.95,68.32 L86.95,71.43 L92.95,61.52 L98.95,60.95 L104.95,57.51 L110.95,56.83
		L116.95,55.96 L122.94,53.06 L128.94,59.62 L134.94,56.12 L140.94,48.07 L146.94,52.51 L152.94,50.76 L158.94,44.24
		L164.93,47.76 L170.93,42.69 L176.93,48.65 L182.93,36.12 L188.93,37.67 L194.93,33.59 L200.92,38.63 L206.92,32.23
		L212.92,36.02 L218.92,39.28 L224.92,32.48 L230.92,32.98 L236.92,27.09 L242.91,34.49 L248.91,29.55 L254.91,28.57
		L260.91,26.74 L266.91,32.50 L272.91,28.49 L278.90,30.28 L284.90,24.49 L290.90,26.47 L296.90,22.47 L302.90,26.01
		L308.90,22.85 L314.90,28.86 L320.89,26.68 L326.89,28.70 L332.89,26.03 L338.89,32.72 L344.89,27.73 L350.89,27.68
		L356.89,22.93 L362.88,28.63 L368.88,32.21 L374.88,29.51 L380.88,25.09 L386.88,28.30 L392.88,35.74 L398.87,31.23
		L404.87,31.01 L410.87,34.60 L416.87,29.79 L422.87,36.05 L428.87,39.77 L434.87,34.36 L440.86,41.94 L446.86,39.92
		L452.86,38.45 L458.86,45.40 L464.86,42.44 L470.86,44.18 L476.85,43.54 L482.85,44.04 L488.85,52.38 L494.85,55.11
		L500.85,49.94 L506.85,51.66 L512.85,57.23 L518.84,60.21 L524.84,58.85 L530.84,59.28 L536.84,62.21 L542.84,60.71
		L548.84,67.34 L554.84,66.67 L560.83,67.95 L566.83,78.88 L572.83,81.99 L578.83,75.31 L584.83,86.52 L590.83,90.87
		L596.82,86.32 L602.82,84.29 L608.82,97.47 L614.82,99.54  '/></g>
	</g>
<g fill="none" color="white" stroke="rgb(  0, 128, 255)" stroke-width="2.00" stroke-linecap="butt" stroke-linejoin="miter">
</g>
<g fill="none" color="black" stroke="currentColor" stroke-width="2.00" stroke-linecap="butt" stroke-linejoin="miter">
</g>
<g fill="none" color="black" stroke="black" stroke-width="4.00" stroke-linecap="butt" stroke-linejoin="miter">
</g>
<g fill="none" color="black" stroke="currentColor" stroke-width="4.00" stroke-linecap="butt" stroke-linejoin="miter">
</g>
<g fill="none" color="black" stroke="black" stroke-width="2.00" stroke-linecap="butt" stroke-linejoin="miter">
</g>
<g fill="none" color="black" stroke="currentColor" stroke-width="2.00" stroke-linecap="butt" stroke-linejoin="miter">
</g>
</g>

    </symbol>


"""

svg_tail = "</svg>"

svg = svg_base

label_ndigits = 5
x0 = 0.5 # inch
y0 = 0.3125
xstride = 2.0
ystride = 0.79375
xsize = xstride
ysize = ystride - 1/16

label_i = 450

def main():
    global svg
    global label_i

    for i in range(50):
        li = label_i + i
        qr_url = url_base + f"{label_i:0{label_ndigits}d}"
        svg += f"""
    <g id="label{li}">
      <!-- Contents of your smaller SVG go here -->
      <use xlink:href="#logo" transform="translate(6, 7) scale(0.08)" />
      <text x="10" y="60" dominant-baseline="middle" text-anchor="left"
            font-family="Arial" font-size="15" font-weight="bold">
        https://www.snr-lab.org/
      </text>
      <text x="123" y="42" dominant-baseline="middle" text-anchor="middle"
            font-family="Arial" font-size="42" font-weight="bold">
        {li:0{label_ndigits}d}
      </text>
    </g>
"""
    svg += "  </defs>\n"
    for iy in range(10):
        for ix in range(5):
            x = x0 + ix * xstride
            y = y0 + iy * ystride
#            svg += f"<rect fill='none' stroke-width='1' stroke='currentColor' x='{x}in' y='{y}in' width='{xsize}in' height='{ysize}in'/>"
            svg += f"<use x='{x}in' y='{y}in' xlink:href='#label{label_i}' />"

            label_i += 1

    svg += svg_tail
    with open("stickerT.svg", "w") as f:
        f.write(svg)

if __name__ == "__main__":
    main()
