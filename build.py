"""Builds banner.svg by embedding your molecule render.
Usage: python build.py [path/to/banner.png]   (default: banner.png next to this file)"""
import base64, io, sys, os
from PIL import Image

src = sys.argv[1] if len(sys.argv) > 1 else "banner.png"
im = Image.open(src).convert("RGB")
im.thumbnail((1400, 1400))
buf = io.BytesIO(); im.save(buf, "JPEG", quality=86, optimize=True)
b64 = base64.b64encode(buf.getvalue()).decode()
W, H = im.size
CW = 630; CH = round(CW * H / W)          # image card size
CX, CY = 626, (420 - CH) // 2              # card position
sx, sy = CW / W, CH / H                    # for mapping contact lines (tuned for the 1007x500 crop)

def P(x, y):  # map crop coords (1007x500 basis) to banner coords
    return f"{CX + x/1007*CW:.1f},{CY + y/500*CH:.1f}"

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1280" height="420" viewBox="0 0 1280 420" role="img" aria-label="Debarshi Bose — Structural Biochemistry and Computational Biophysics">
<title>Debarshi Bose — Structural Biochemistry &amp; Computational Biophysics</title>
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#070A14"/><stop offset="1" stop-color="#03040A"/></linearGradient>
  <radialGradient id="gA" cx="0.78" cy="0.45" r="0.55"><stop offset="0" stop-color="#8F8CE0" stop-opacity=".30"/><stop offset="1" stop-color="#8F8CE0" stop-opacity="0"/></radialGradient>
  <radialGradient id="gB" cx="0.95" cy="0.95" r="0.45"><stop offset="0" stop-color="#F2A03D" stop-opacity=".22"/><stop offset="1" stop-color="#F2A03D" stop-opacity="0"/></radialGradient>
  <radialGradient id="gC" cx="0.05" cy="0.0" r="0.5"><stop offset="0" stop-color="#3FA9F5" stop-opacity=".18"/><stop offset="1" stop-color="#3FA9F5" stop-opacity="0"/></radialGradient>
  <pattern id="dots" width="28" height="28" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="#9db0ff" opacity=".13"/></pattern>

  <!-- molecule: white page -> dark, hues preserved -->
  <filter id="night" color-interpolation-filters="sRGB" x="0" y="0" width="1" height="1">
    <feColorMatrix type="matrix" values="-1 0 0 0 1  0 -1 0 0 1  0 0 -1 0 1  0 0 0 1 0"/>
    <feColorMatrix type="hueRotate" values="180"/>
    <feComponentTransfer><feFuncR type="gamma" amplitude="1.12" exponent="0.9"/><feFuncG type="gamma" amplitude="1.12" exponent="0.9"/><feFuncB type="gamma" amplitude="1.12" exponent="0.9"/></feComponentTransfer>
  </filter>
  <linearGradient id="fadeL" x1="0" x2="1" y1="0" y2="0"><stop offset="0" stop-color="#000"/><stop offset=".30" stop-color="#fff"/><stop offset=".92" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity=".55"/></linearGradient>
  <mask id="mfade" maskUnits="userSpaceOnUse" x="{CX}" y="{CY}" width="{CW}" height="{CH}"><rect x="{CX}" y="{CY}" width="{CW}" height="{CH}" fill="url(#fadeL)"/></mask>
  <clipPath id="card"><rect x="{CX}" y="{CY}" width="{CW}" height="{CH}" rx="20"/></clipPath>
  <linearGradient id="sweep" x1="0" x2="1" y1="0" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#cfd6ff" stop-opacity=".16"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
  <linearGradient id="rim" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3FA9F5"/><stop offset=".5" stop-color="#8F8CE0"/><stop offset="1" stop-color="#F2A03D"/></linearGradient>
  <linearGradient id="nameG" x1="0" x2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#C9C7F5"/></linearGradient>
  <clipPath id="whole"><rect width="1280" height="420" rx="18"/></clipPath>
</defs>
<style>
  .name{{font:700 64px Georgia,'Times New Roman',serif;letter-spacing:.5px}}
  .sub{{font:600 20px 'Segoe UI',-apple-system,Helvetica,Arial,sans-serif;fill:#C7CBE8;letter-spacing:.3px}}
  .role{{font:500 17px 'Segoe UI',-apple-system,Helvetica,Arial,sans-serif;fill:#F2B25C;opacity:0}}
  .pill{{font:600 13.5px 'Segoe UI',-apple-system,Helvetica,Arial,sans-serif;fill:#DCE0FF}}
  .hb{{stroke-linecap:round;fill:none;stroke-dasharray:5 6;animation:flow 1.6s linear infinite}}
  .hr{{stroke:#FF5C6C;stroke-width:2}} .hp{{stroke:#B48CFF;stroke-width:2}}
  .zoom{{transform-origin:{CX+CW/2}px {CY+CH/2}px;animation:kb 18s ease-in-out infinite alternate}}
  .sweep{{animation:sw 9s ease-in-out infinite}}
  .rim{{stroke-dasharray:140 1900;animation:rimrun 7s linear infinite}}
  .float{{animation:fl 7s ease-in-out infinite alternate}}
  @keyframes flow{{to{{stroke-dashoffset:-22}}}}
  @keyframes kb{{from{{transform:scale(1.00) translate(0,0)}}to{{transform:scale(1.07) translate(-8px,-4px)}}}}
  @keyframes sw{{0%,55%{{transform:translateX(-{CW}px)}}100%{{transform:translateX({CW*2}px)}}}}
  @keyframes rimrun{{to{{stroke-dashoffset:-2040}}}}
  @keyframes fl{{from{{transform:translateY(0)}}to{{transform:translateY(-10px)}}}}
  @media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
</style>

<g clip-path="url(#whole)">
  <rect width="1280" height="420" fill="url(#bg)"/>
  <rect width="1280" height="420" fill="url(#gA)"/><rect width="1280" height="420" fill="url(#gB)"/><rect width="1280" height="420" fill="url(#gC)"/>
  <rect width="1280" height="420" fill="url(#dots)"/>

  <!-- molecule card -->
  <g mask="url(#mfade)">
    <g clip-path="url(#card)">
      <g class="zoom">
        <image x="{CX}" y="{CY}" width="{CW}" height="{CH}" preserveAspectRatio="xMidYMid slice" filter="url(#night)" href="data:image/jpeg;base64,{b64}"/>
        <!-- polar contacts, echoing the dashed H-bonds in the render -->
        <path class="hb hr" d="M{P(390,75)} L{P(520,30)}"/>
        <path class="hb hp" d="M{P(385,100)} L{P(430,112)}"/>
        <path class="hb hp" d="M{P(715,105)} L{P(770,128)}" style="animation-duration:2.1s"/>
        <path class="hb hp" d="M{P(940,200)} L{P(965,158)}" style="animation-duration:1.9s"/>
        <path class="hb hr" d="M{P(738,440)} L{P(742,498)}" style="animation-duration:2.4s"/>
      </g>
      <rect class="sweep" x="{CX}" y="{CY}" width="{CW*0.35:.0f}" height="{CH}" fill="url(#sweep)"/>
    </g>
  </g>
  <rect x="{CX}" y="{CY}" width="{CW}" height="{CH}" rx="20" fill="none" stroke="#8F8CE0" stroke-opacity=".18" stroke-width="1.2"/>
  <rect class="rim" x="{CX}" y="{CY}" width="{CW}" height="{CH}" rx="20" fill="none" stroke="url(#rim)" stroke-width="2.2" stroke-linecap="round" pathLength="2040"/>

  <!-- text -->
  <g transform="translate(72,0)">
    <text class="name" x="0" y="168" fill="url(#nameG)">Debarshi Bose</text>
    <text class="sub" x="2" y="206">Structural Biochemistry &amp; Computational Biophysics</text>

    <g>
      <text class="role" x="2" y="248">Allostery and conformational switching in photoreceptors
        <animate attributeName="opacity" values="0;1;1;0;0" keyTimes="0;.04;.30;.34;1" dur="12s" repeatCount="indefinite"/></text>
      <text class="role" x="2" y="248">Rational design of next-generation optogenetic tools
        <animate attributeName="opacity" values="0;1;1;0;0" keyTimes="0;.04;.30;.34;1" dur="12s" begin="4s" repeatCount="indefinite"/></text>
      <text class="role" x="2" y="248">Molecular dynamics, tested at the bench
        <animate attributeName="opacity" values="0;1;1;0;0" keyTimes="0;.04;.30;.34;1" dur="12s" begin="8s" repeatCount="indefinite"/></text>
    </g>

    <g transform="translate(0,282)">
      <rect width="388" height="40" rx="20" fill="#8F8CE0" fill-opacity=".10" stroke="#8F8CE0" stroke-opacity=".55"/>
      <circle cx="22" cy="20" r="5" fill="#5BE3A0"><animate attributeName="opacity" values="1;.25;1" dur="2.2s" repeatCount="indefinite"/><animate attributeName="r" values="4.5;6.5;4.5" dur="2.2s" repeatCount="indefinite"/></circle>
      <text class="pill" x="40" y="25">Applying for Fall 2027 PhD programs</text>
    </g>
    <text class="pill" x="2" y="352" style="fill:#8E94BF;font-weight:500">Presidency University, Kolkata  ·  M.Sc. Life Sciences</text>
  </g>

  <g class="float" opacity=".7">
    <circle cx="520" cy="70" r="3" fill="#3FA9F5"/><circle cx="548" cy="350" r="2.4" fill="#F2A03D"/><circle cx="1238" cy="60" r="2.6" fill="#8F8CE0"/>
  </g>
  <rect width="1280" height="420" rx="18" fill="none" stroke="#8F8CE0" stroke-opacity=".22"/>
</g>
</svg>'''
open("banner.svg", "w").write(svg)
print("banner.svg", len(svg)//1024, "KB")
