
import re

file_path = r'd:\IQH_Project\heathcare_itsdone\index2.html'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
print(f"Line 3109: {lines[3108].strip()[:80]}")
print(f"Line 3335: {lines[3334].strip()[:80]}")

# New banner block to insert (lines 3109-3335, i.e. indices 3108-3334 inclusive)
new_banner = r"""    <!-- Why Patients Choose Us -->
    <section id="why-choose-us" class="overflow-hidden">

      <!-- ── TOP BANNER — pixel-perfect clone of Image 1 ── -->
      <style>
        #wcu-banner {
          position:relative;
          overflow:hidden;
          background: linear-gradient(110deg, #1c0d6e 0%, #1a3da8 25%, #1565c0 45%, #0d7fa5 68%, #05afc2 100%);
        }
        #wcu-bg-img {
          position:absolute;inset:0;
          background:url('https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=1400&q=35&auto=format&fit=crop') center/cover no-repeat;
          opacity:0.11;
          mix-blend-mode:luminosity;
        }
        #wcu-left-shadow {
          position:absolute;top:0;left:0;bottom:0;width:36%;
          background:linear-gradient(to right,rgba(20,8,90,0.88) 0%,rgba(20,8,90,0.35) 70%,transparent 100%);
          pointer-events:none;
        }
        #wcu-right-glow {
          position:absolute;top:0;right:0;bottom:0;width:38%;
          background:linear-gradient(to left,rgba(5,175,194,0.45) 0%,transparent 100%);
          pointer-events:none;
        }
        .wcu-img-cell {
          border-radius:8px;
          overflow:hidden;
          border:1px solid rgba(255,255,255,0.18);
        }
        .wcu-img-cell img { width:100%;height:100%;object-fit:cover;display:block; }
        .wcu-ring {
          width:76px;height:76px;border-radius:50%;
          border:3px solid rgba(255,255,255,0.32);
          background:rgba(255,255,255,0.11);
          backdrop-filter:blur(4px);
          display:flex;align-items:center;justify-content:center;
          position:relative;flex-shrink:0;
        }
        .wcu-ring svg {
          position:absolute;inset:-5px;
          width:calc(100% + 10px);height:calc(100% + 10px);
          animation:WCUspin 10s linear infinite;
        }
        @keyframes WCUspin { to { transform:rotate(360deg); } }
        .wcu-pill-img1 {
          display:block;
          width:100%;
          text-align:center;
          padding:0.52rem 1.4rem;
          border-radius:999px;
          background:rgba(13,160,190,0.45);
          border:1.5px solid rgba(100,220,240,0.45);
          backdrop-filter:blur(6px);
          color:#fff;
          font-weight:600;
          font-size:0.83rem;
          letter-spacing:0.015em;
          transition:background 0.2s,transform 0.15s;
          white-space:nowrap;
          text-decoration:none;
        }
        .wcu-pill-img1:hover {
          background:rgba(13,180,210,0.82);
          transform:scale(1.02);
          color:#fff;
        }
      </style>

      <div id="wcu-banner">
        <div id="wcu-bg-img"></div>
        <div id="wcu-left-shadow"></div>
        <div id="wcu-right-glow"></div>

        <div class="relative z-10 flex flex-col lg:flex-row items-stretch w-full" style="min-height:295px;">

          <!-- ① LEFT: 2×3 Image Grid — matches Image 1 left panel exactly -->
          <div class="hidden lg:grid grid-cols-2 grid-rows-3 gap-[7px] p-[10px] shrink-0" style="width:210px;">
            <!-- Row 1: full-width team photo -->
            <div class="wcu-img-cell col-span-2" style="height:82px;">
              <img src="https://images.unsplash.com/photo-1582750433449-648ed127bb54?w=420&q=70&auto=format&fit=crop&crop=faces" alt="Medical team">
            </div>
            <!-- Row 2 -->
            <div class="wcu-img-cell" style="height:66px;">
              <img src="https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=200&q=70&auto=format&fit=crop" alt="Medical">
            </div>
            <div class="wcu-img-cell" style="height:66px;">
              <img src="https://images.unsplash.com/photo-1584820927498-cfe5211fd8bf?w=200&q=70&auto=format&fit=crop" alt="Tools">
            </div>
            <!-- Row 3 -->
            <div class="wcu-img-cell" style="height:66px;">
              <img src="https://images.unsplash.com/photo-1551601651-2a8555f1a136?w=200&q=70&auto=format&fit=crop&crop=faces" alt="Doctors">
            </div>
            <div class="wcu-img-cell" style="height:66px;">
              <img src="https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?w=200&q=70&auto=format&fit=crop" alt="Hospital">
            </div>
          </div>

          <!-- ② CENTER: 24h animated ring + WHY CHOOSE US? heading + 4 centred pill buttons + phone CTA -->
          <div class="flex flex-col justify-center py-7 lg:py-5 px-6 lg:px-8" style="flex:0 0 auto; width:min(100%,380px);">

            <!-- 24h Ring badge + Heading row -->
            <div class="flex items-center gap-4 mb-5">
              <div class="wcu-ring">
                <div class="text-center z-10 leading-none" style="position:relative;">
                  <span class="text-white font-black" style="font-size:1.2rem;line-height:1.1;">24</span><br>
                  <span class="font-bold uppercase text-white" style="font-size:0.44rem;letter-spacing:0.12em;opacity:0.7;">h</span>
                </div>
                <svg viewBox="0 0 86 86" fill="none">
                  <circle cx="43" cy="43" r="38" stroke="rgba(255,255,255,0.55)" stroke-width="2.5" stroke-dasharray="7 5" stroke-linecap="round"/>
                </svg>
              </div>
              <div>
                <h2 class="text-white font-black uppercase leading-tight" style="font-size:clamp(1.2rem,2vw,1.7rem);letter-spacing:0.025em;">
                  WHY CHOOSE <span style="color:#7dd3fc;">US?</span>
                </h2>
              </div>
            </div>

            <!-- 4 centred pill buttons — text-only, centred, exactly matching Image 1 -->
            <div class="flex flex-col gap-[10px]">
              <a href="#why-choose-detail" class="wcu-pill-img1">Savings on Consultation &amp; Procedures</a>
              <a href="#why-choose-detail" class="wcu-pill-img1">Reach a Nearby Hospital Fast</a>
              <a href="#why-choose-detail" class="wcu-pill-img1">Transparent Cost Discussion</a>
              <a href="#why-choose-detail" class="wcu-pill-img1">Experienced Specialists</a>
            </div>

            <!-- Phone CTA -->
            <div class="mt-6 flex items-center gap-3">
              <div style="width:42px;height:42px;border-radius:50%;background:rgba(255,255,255,0.13);border:2px solid rgba(255,255,255,0.32);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
                <span class="material-symbols-outlined text-white" style="font-size:1.1rem;">call</span>
              </div>
              <div>
                <p class="text-white/55 font-bold uppercase" style="font-size:0.58rem;letter-spacing:0.1em;margin:0 0 1px;">Call To Find Us</p>
                <a href="tel:9795758345" class="text-white font-black hover:text-sky-200 transition-colors" style="font-size:1.3rem;letter-spacing:0.02em;">9795758345</a>
              </div>
            </div>
          </div>

          <!-- ③ DOCTOR IMAGE — bleeds between center and right, exactly like Image 1 -->
          <div class="hidden xl:block relative shrink-0 self-stretch overflow-hidden" style="width:210px;flex-grow:1;max-width:230px;">
            <img
              src="https://images.unsplash.com/photo-1559839734-2b71ea197ec2?w=500&q=80&auto=format&fit=crop&crop=top"
              alt="IQH Doctor"
              style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:top;
                     -webkit-mask-image:linear-gradient(to right,transparent 0%,black 22%,black 74%,transparent 100%);
                     mask-image:linear-gradient(to right,transparent 0%,black 22%,black 74%,transparent 100%);">
          </div>

          <!-- ④ RIGHT: IQH branding — mirrors "Savitri Trust Care Hospital" big-text panel -->
          <div class="hidden xl:flex flex-col justify-center py-8 shrink-0" style="width:300px;padding-left:0.75rem;padding-right:2.5rem;background:linear-gradient(to left,rgba(5,165,195,0.5) 0%,transparent 100%);">
            <img src="assets/img/IQH.png" alt="IQH" style="height:34px;margin-bottom:12px;object-fit:contain;object-position:left;filter:brightness(0) invert(1);opacity:0.9;">
            <!-- Large hospital-name-style heading -->
            <h3 class="text-white font-black leading-[1.06]" style="font-size:clamp(1.55rem,2.5vw,2.45rem);margin-bottom:10px;">
              Your Trusted<br>Healthcare<br><span style="color:#7dd3fc;">Portal!</span>
            </h3>
            <!-- Tagline in teal -->
            <p class="font-bold" style="color:#7dd3fc;font-size:0.88rem;margin-bottom:10px;">Your Path To Optimal Health!</p>
            <!-- Description -->
            <p class="text-white/65 leading-relaxed" style="font-size:0.77rem;max-width:240px;">
              We are committed to improving the wellbeing of you and your family and providing the best medical care that empowers you and your family to live life to the fullest.
            </p>
          </div>

        </div>
      </div>
      <!-- ── END TOP BANNER ── -->
"""

# Replace lines 3109-3335 (0-indexed: 3108 to 3334)
new_lines = lines[:3108] + [new_banner] + lines[3335:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

# Verify
with open(file_path, 'r', encoding='utf-8') as f:
    result = f.readlines()

print(f"New total lines: {len(result)}")
print(f"New line 3109: {result[3108].strip()[:80]}")
print("Done!")
