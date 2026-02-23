import re

with open('cornia.html', encoding='utf-8') as f:
    content = f.read()

new_sections = '''    <!-- SYMPTOMS SECTION: dark full-bleed split -->
    <section class="symptoms-section-bg">
        <div class="symptoms-grid">

            <!-- LEFT: dark content panel -->
            <div class="sym-left-panel">
                <span class="section-tag" style="margin-bottom:20px;">Warning Signs</span>
                <h2 class="section-title" style="margin-bottom:10px;">
                    Symptoms of <span class="brand-pink">Cornea</span><br>
                    <span class="brand-gradient">Diseases</span>
                </h2>
                <p class="sym-intro">Corneal symptoms can appear suddenly or gradually. Recognise these early warning signs and seek timely specialist care.</p>

                <ul class="symptom-list">
                    <li>
                        <div class="sym-num">01</div>
                        <div class="sym-text">
                            <strong>Eye Pain &amp; Redness</strong>
                            <span>Persistent pain or visible redness in one or both eyes</span>
                        </div>
                        <span class="sym-arrow">&#8250;</span>
                    </li>
                    <li>
                        <div class="sym-num">02</div>
                        <div class="sym-text">
                            <strong>Blurred or Cloudy Vision</strong>
                            <span>Sudden or gradual loss of sharpness, especially in bright light</span>
                        </div>
                        <span class="sym-arrow">&#8250;</span>
                    </li>
                    <li>
                        <div class="sym-num">03</div>
                        <div class="sym-text">
                            <strong>Sensitivity to Light</strong>
                            <span>Discomfort or pain in sunlight or artificial lighting (photophobia)</span>
                        </div>
                        <span class="sym-arrow">&#8250;</span>
                    </li>
                    <li>
                        <div class="sym-num">04</div>
                        <div class="sym-text">
                            <strong>Excessive Blinking</strong>
                            <span>Uncontrolled or frequent blinking as an involuntary response to irritation</span>
                        </div>
                        <span class="sym-arrow">&#8250;</span>
                    </li>
                    <li>
                        <div class="sym-num">05</div>
                        <div class="sym-text">
                            <strong>Foreign Body Sensation</strong>
                            <span>Feeling of something stuck in the eye even when nothing is present</span>
                        </div>
                        <span class="sym-arrow">&#8250;</span>
                    </li>
                </ul>

                <div class="conditions-note">
                    <strong>Common conditions:</strong> Keratitis (infection-driven inflammation), Keratoconus (corneal thinning), and corneal ulcers &mdash; all require prompt medical evaluation.
                </div>
            </div>

            <!-- RIGHT: full-height photo -->
            <div class="visual-eye-box">
                <img
                    src="https://images.unsplash.com/photo-1559757175-0eb30cd8c063?auto=format&fit=crop&w=900&q=85"
                    alt="Close-up of human eye - cornea treatment"
                    style="width:100%; height:100%; object-fit:cover; position:absolute; inset:0; display:block;"
                    loading="lazy"
                />
                <div style="position:absolute; inset:0; background: linear-gradient(to right, #0d0d1a 0%, transparent 28%); pointer-events:none;"></div>
                <div style="position:absolute; inset:0; background: linear-gradient(to top, rgba(13,13,26,0.85) 0%, transparent 55%); pointer-events:none;"></div>
                <div style="position:absolute; top:24px; right:24px; background:rgba(13,13,26,0.65); backdrop-filter:blur(12px); border:1px solid rgba(255,255,255,0.13); color:white; font-size:12px; font-weight:600; padding:8px 16px; border-radius:50px; display:flex; align-items:center; gap:8px;">
                    <span style="width:8px;height:8px;border-radius:50%;background:#e91e8c;display:inline-block;"></span>
                    Cornea Anatomy
                </div>
                <div style="position:absolute; bottom:28px; left:28px; right:28px; display:flex; gap:10px; flex-wrap:wrap;">
                    <div style="background:rgba(233,30,140,0.15); border:1px solid rgba(233,30,140,0.4); backdrop-filter:blur(8px); color:#f9a8d4; font-size:12px; font-weight:600; padding:6px 14px; border-radius:50px;">Iris</div>
                    <div style="background:rgba(92,45,142,0.15); border:1px solid rgba(92,45,142,0.45); backdrop-filter:blur(8px); color:#c4b5fd; font-size:12px; font-weight:600; padding:6px 14px; border-radius:50px;">Pupil</div>
                    <div style="background:rgba(41,121,255,0.12); border:1px solid rgba(41,121,255,0.35); backdrop-filter:blur(8px); color:#93c5fd; font-size:12px; font-weight:600; padding:6px 14px; border-radius:50px;">Sclera</div>
                    <div style="background:rgba(255,255,255,0.07); border:1px solid rgba(255,255,255,0.12); backdrop-filter:blur(8px); color:rgba(255,255,255,0.55); font-size:12px; font-weight:600; padding:6px 14px; border-radius:50px;">Cornea</div>
                </div>
            </div>

        </div>
    </section>


    <!-- CONDITIONS SECTION: bento grid -->
    <section class="conditions-section">
        <div class="cond-header">
            <div>
                <span class="section-tag" style="margin-bottom:14px;">Conditions We Treat</span>
                <h2 class="section-title">Types of <span class="brand-pink">Cornea</span> <span class="brand-gradient">Conditions</span></h2>
            </div>
            <p class="cond-header-right">Conditions affecting the cornea can vary greatly in severity. Early diagnosis is key to effective treatment.</p>
        </div>

        <div class="cond-top-row">
            <div class="condition-card c1" style="background: linear-gradient(135deg, #fff0f7, #fff); display:flex; gap:28px; align-items:flex-start;">
                <div style="font-size:52px; line-height:1; flex-shrink:0;">&#129440;</div>
                <div>
                    <div style="font-size:11px; font-weight:700; letter-spacing:2px; text-transform:uppercase; color:#e91e8c; margin-bottom:10px;">Most Common</div>
                    <h3 style="font-size:20px; font-weight:800; color:#0d0d1a; margin-bottom:10px;">Infections</h3>
                    <p style="font-size:14px; color:#374151; line-height:1.8;">Bacterial, viral or fungal infections can lead to painful corneal ulcers that require prompt medical attention. Keratitis is the most prevalent form and responds well to early treatment.</p>
                </div>
            </div>
            <div class="condition-card c2" style="background: linear-gradient(135deg, #f5f0ff, #fff);">
                <div style="font-size:40px; margin-bottom:16px;">&#128300;</div>
                <h3 style="font-size:17px; font-weight:800; color:#0d0d1a; margin-bottom:10px;">Degenerative Conditions</h3>
                <p style="font-size:13.5px; color:#374151; line-height:1.75;">Keratoconus or Fuchs\' dystrophy slowly damages the cornea over time and diminishes vision progressively.</p>
            </div>
            <div class="condition-card c3" style="background: linear-gradient(135deg, #eff6ff, #fff);">
                <div style="font-size:40px; margin-bottom:16px;">&#9889;</div>
                <h3 style="font-size:17px; font-weight:800; color:#0d0d1a; margin-bottom:10px;">Trauma</h3>
                <p style="font-size:13.5px; color:#374151; line-height:1.75;">Physical damage from accidents or chemical burns can cause corneal scarring, sometimes permanently affecting vision.</p>
            </div>
        </div>

        <div class="cond-bottom-row">
            <div class="condition-card c4" style="background: linear-gradient(135deg, #fffbeb, #fff);">
                <div style="font-size:40px; margin-bottom:16px;">&#129518;</div>
                <h3 style="font-size:17px; font-weight:800; color:#0d0d1a; margin-bottom:10px;">Genetic Disorders</h3>
                <p style="font-size:13.5px; color:#374151; line-height:1.75;">Congenital dystrophies and other hereditary conditions can impact vision quality early in life.</p>
            </div>
            <div class="condition-card c5" style="background: linear-gradient(135deg, #ecfdf5, #fff);">
                <div style="font-size:40px; margin-bottom:16px;">&#127807;</div>
                <h3 style="font-size:17px; font-weight:800; color:#0d0d1a; margin-bottom:10px;">Allergies</h3>
                <p style="font-size:13.5px; color:#374151; line-height:1.75;">Severe allergies can break down the ocular surface and cause chronic irritation and discomfort.</p>
            </div>
            <div style="border-radius:20px; border:1px solid #1a0a2e; background: linear-gradient(135deg, #0d0d1a, #1a0a2e); padding:34px 30px; display:flex; flex-direction:column; justify-content:space-between;">
                <div style="font-size:11px; font-weight:700; letter-spacing:1.5px; text-transform:uppercase; color:rgba(233,30,140,0.8); margin-bottom:16px;">Our Promise</div>
                <p style="font-size:15px; color:rgba(255,255,255,0.75); line-height:1.75; flex:1;">Every corneal condition we treat is approached with precision diagnostics and personalised care plans.</p>
                <div style="margin-top:24px; display:inline-flex; align-items:center; gap:8px; color:#e91e8c; font-size:13px; font-weight:700; cursor:pointer;">Book a Consultation <span style="font-size:18px;">&#8594;</span></div>
            </div>
        </div>
    </section>'''

# Find start marker
start_marker = '<!-- SYMPTOMS'
# Find end marker (end of conditions section closing tag)
# We need to replace from <section class="symptoms-section-bg"> to </section> for conditions

# Use regex to replace both sections
pattern = r'<!-- (?:SYMPTOMS|═+ SYMPTOMS).*?</section>\s*\n\s*\n\s*<!-- (?:CONDITIONS|═+ TYPES OF CONDITIONS).*?</section>'
result = re.sub(pattern, new_sections.strip(), content, flags=re.DOTALL)

if result == content:
    print("PATTERN NOT MATCHED - trying alternate markers")
    # Try simpler approach
    start = content.find('<section class="symptoms-section-bg">')
    # Find the end of the second section (after conditions-grid)
    conditions_end_marker = '<!-- ══ BENEFITS'
    end = content.find(conditions_end_marker)
    if start != -1 and end != -1:
        result = content[:start] + new_sections + '\n\n\n    ' + content[end:]
        print(f"Replaced from index {start} to {end}")
    else:
        print(f"start={start}, end={end}")
else:
    print("Regex replacement successful")

with open('cornia.html', 'w', encoding='utf-8') as f:
    f.write(result)

print("Done")
