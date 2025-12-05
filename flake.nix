{
  description = "Dev shell";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }: {
    devShells.x86_64-linux.default = let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };
    in pkgs.mkShell {
      name = "dev shell";

      packages = with pkgs; [
        python312
        poetry
        zlib
        gcc
        mtdev
        mesa
        libGL
        libxkbcommon
        SDL2
      ];

      # Export LD_LIBRARY_PATH so Python (NumPy, etc.) can see system libs
      LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
        pkgs.zlib
        pkgs.mtdev
        pkgs.libGL
        pkgs.libxkbcommon
        pkgs.mesa
        pkgs.gcc.cc.lib
      ];

      shellHook = ''
        echo "installation completed"
      '';
    };
  };
}

